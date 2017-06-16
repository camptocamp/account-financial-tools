# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, _
from odoo.exceptions import UserError


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.multi
    def write(self, vals):
        for line in self:
            if line.move_id or vals.get('move_id'):
                # if we have a move line, then it is not a timesheet line
                continue
            # We are assuming there is one employee per user
            employee_id = self.env['res.users'].browse(
                self.env.uid).employee_ids[0]
            if not employee_id.analytic_tag_id:
                raise UserError(_("You must be linked to a business unit in "
                                  "in order to create timesheet lines"))
            vals['tag_ids'] = [(4, employee_id.analytic_tag_id.id)]
        return super(AccountAnalyticLine, self).write(vals)

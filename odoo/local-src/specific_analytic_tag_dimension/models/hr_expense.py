# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic Account',
        required=True,
        states={'post': [('readonly', True)], 'done': [('readonly', True)]},
        oldname='analytic_account'
    )

    def _prepare_move_line(self, line):
        res = super(HrExpense, self)._prepare_move_line(line)
        res['analytic_tag_ids'] = [
            (4, self.employee_id.analytic_tag_id.id)]
        return res

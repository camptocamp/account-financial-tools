# -*- coding: utf-8 -*-
# Author: Camptocamp SA
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    analytic_amount = fields.Float(
        string="Analytic amount",
        compute="_compute_analytic_amount",
    )

    @api.multi
    def _compute_analytic_amount(self):
        for record in self:
            record.analytic_amount = record.analytic_account_id.balance

    def action_view_analytic_line(self):
        action = self.env.ref('analytic.account_analytic_line_action')
        result = action.read()[0]
        result['context'] = {'default_account_id': self.analytic_account_id.id}
        return result

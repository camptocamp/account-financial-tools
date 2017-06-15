# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    analytic_tag_id = fields.Many2one(
        'account.analytic.tag',
        string='Business Unit',
        required=True,
    )

    @api.onchange('department_id')
    def _onchange_department_id(self):
        if self.department_id:
            self.analytic_tag_id = self.department_id.analytic_tag_id

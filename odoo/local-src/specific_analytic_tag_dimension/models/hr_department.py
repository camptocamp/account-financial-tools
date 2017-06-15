# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HrDepartment(models.Model):
    _inherit = 'hr.department'

    analytic_tag_id = fields.Many2one(
        'account.analytic.tag',
        string='Business Unit',
        required=True,
    )

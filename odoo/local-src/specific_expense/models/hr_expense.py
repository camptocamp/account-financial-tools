# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HrEpense(models.Model):
    _inherit = 'hr.expense'

    prd_company_id = fields.Many2one(
        'res.company',
        string='Field Label',
        related='product_id.company_id',
    )

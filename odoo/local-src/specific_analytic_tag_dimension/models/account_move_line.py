# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    product_category_id = fields.Many2one(
        'product.category',
        related='product_id.categ_id',
        readonly=True,
        string='Category',
    )

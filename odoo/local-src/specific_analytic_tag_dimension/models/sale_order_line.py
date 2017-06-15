# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    analytic_tag_ids = fields.Many2many(
        'account.analytic.tag',
        required=True,
    )

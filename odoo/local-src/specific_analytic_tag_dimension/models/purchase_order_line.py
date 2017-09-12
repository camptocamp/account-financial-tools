# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    analytic_tag_ids = fields.Many2many(
        'account.analytic.tag',
        readonly=True,
        compute='compute_tag'
    )
    analytic_tag_id = fields.Many2one(
        'account.analytic.tag',
        required=True,
    )

    @api.onchange('analytic_tag_id')
    def compute_tag(self):
        for line in self:
            line.analytic_tag_ids = line.analytic_tag_id

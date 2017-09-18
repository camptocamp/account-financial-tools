# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    analytic_tag_ids = fields.Many2many(
        'account.analytic.tag',
        readonly=True,
    )
    analytic_tag_id = fields.Many2one(
        'account.analytic.tag',
        required=True,
        compute='_compute_tag',
        inverse='_set_tag',
        domain=[('analytic_dimension_id', '!=', False)],
    )

    @api.depends('analytic_tag_ids')
    def _compute_tag(self):
        for line in self:
            tags = line.analytic_tag_ids.filtered('analytic_dimension_id')
            if tags:
                line.analytic_tag_id = tags[0]
            else:
                line.analytic_tag_id = False

    def _set_tag(self):
        for line in self:
            line.analytic_tag_ids += line.analytic_tag_id

# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    amount_delivered = fields.Float(
        string="Amount delivered",
        compute="_compute_amount_delivered",
        store=True,
    )

    amount_invoiced = fields.Float(
        string="Amount invoiced",
        compute="_compute_amount_invoiced",
        store=True,
    )

    company_currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="company_id.currency_id",
        store=True,
        readonly=True,
    )

    holding_currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="order_id.holding_currency_id",
        store=True,
        readonly=True,
    )

    amount_delivered_currency = fields.Monetary(
        currency_field="company_currency_id",
        string="Amount delivered currency",
        compute="_compute_amount_delivered_currency",
        store=True,
    )

    amount_invoiced_currency = fields.Monetary(
        currency_field="company_currency_id",
        string="Amount invoiced currency",
        compute="_compute_amount_invoiced_currency",
        store=True,
    )

    amount_delivered_holding_currency = fields.Monetary(
        currency_field="holding_currency_id",
        string="Amount delivered holding currency",
        compute="_compute_amount_delivered_holding_currency",
        store=True,
    )

    amount_invoiced_holding_currency = fields.Monetary(
        currency_field="holding_currency_id",
        string="Amount invoiced holding currency",
        compute="_compute_amount_invoiced_currency",
        store=True,
    )

    @api.depends("qty_delivered", "price_unit")
    def _compute_amount_delivered(self):
        for record in self:
            if record.qty_delivered and record.price_unit:
                record.amount_delivered = record.qty_delivered \
                                          * record.price_unit

    @api.depends("qty_invoiced", "price_unit")
    def _compute_amount_invoiced(self):
        for record in self:
            if record.qty_invoiced and record.price_unit:
                record.amount_invoiced = record.qty_invoiced \
                                          * record.price_unit

    @api.depends("qty_delivered", "price_unit", "company_currency_id")
    def _compute_amount_delivered_currency(self):
        for record in self:
            if record.qty_delivered and record.price_unit:
                result = record.qty_delivered * record.price_unit
                currency_from = record.order_id.pricelist_id.currency_id
                record.amount_delivered_currency = currency_from.compute(
                    result, record.company_currency_id
                )

    @api.depends("qty_invoiced", "price_unit", "company_currency_id")
    def _compute_amount_invoiced_currency(self):
        for record in self:
            if record.qty_invoiced and record.price_unit:
                result = record.qty_invoiced * record.price_unit
                currency_from = record.order_id.pricelist_id.currency_id
                record.amount_invoiced_currency = currency_from.compute(
                    result, record.company_currency_id
                )

    @api.depends("qty_delivered", "price_unit", "holding_currency_id")
    def _compute_amount_delivered_holding_currency(self):
        for record in self:
            if record.qty_delivered and record.price_unit:
                result = record.qty_delivered * record.price_unit
                currency_from = record.order_id.pricelist_id.currency_id
                record.amount_delivered_holding_currency = \
                    currency_from.compute(result, record.holding_currency_id)

    @api.depends("qty_invoiced", "price_unit", "holding_currency_id")
    def _compute_amount_invoiced_holding_currency(self):
        for record in self:
            if record.qty_invoiced and record.price_unit:
                result = record.qty_invoiced * record.price_unit
                currency_from = record.order_id.pricelist_id.currency_id
                record.amount_invoiced_holding_currency = \
                    currency_from.compute(result, record.holding_currency_id)

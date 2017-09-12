# -*- coding: utf-8 -*-
# Author: Denis Leemann
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields
from dateutil.relativedelta import relativedelta


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    date_supplier_warranty_start = fields.Date('Supplier warranty start')
    supplier_warranty_duration = fields.Integer(
        'Supplier warranty',
        help='supplier warranty duration (months)'
    )
    date_supplier_warranty_end = fields.Date(
        'Supplier warranty end',
        compute='_get_supplier_warranty',
        store=True
    )
    date_customer_warranty_start = fields.Date('Customer warranty start')
    customer_warranty_duration = fields.Integer(
        'Customer warranty',
        help='supplier warranty duration (months)'
    )
    date_customer_warranty_end = fields.Date(
        'Customer warranty end',
        compute='_get_customer_warranty',
        store=True
    )
    _sql_constraints = [
        ('positive_supplier_warranty',
         'CHECK (supplier_warranty_duration >= 0)',
         'The supplier warranty duration must be positive',
         ),
        ('positive_customer_warranty',
         'CHECK (customer_warranty_duration >= 0)',
         'The customer warranty duration must be positive',
         )
        ]

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        return super(StockProductionLot, self).name_search(
            name=name,
            args=args,
            operator=operator,
            limit=limit)

    @api.onchange('product_id')
    def onchange_product_id(self):
        for rec in self:
            product = rec.product_id
            if not product:
                rec.supplier_warranty_duration = 0
                rec.customer_warranty_duration = 0
            else:
                rec.supplier_warranty_duration = product.supplier_warranty
                rec.customer_warranty_duration = product.warranty

    @api.depends('date_supplier_warranty_start', 'supplier_warranty_duration')
    def _get_supplier_warranty(self):
        for rec in self:
            if not rec.date_supplier_warranty_start:
                rec.date_supplier_warranty_end = False
            else:
                delta = relativedelta(months=rec.supplier_warranty_duration)
                start = fields.Date.from_string(
                    rec.date_supplier_warranty_start
                )
                end = start + delta
                rec.date_supplier_warranty_end = fields.Date.to_string(end)

    @api.depends('date_customer_warranty_start', 'customer_warranty_duration')
    def _get_customer_warranty(self):
        for rec in self:
            if not rec.date_customer_warranty_start:
                rec.date_customer_warranty_end = False
            else:
                delta = relativedelta(months=rec.customer_warranty_duration)
                start = fields.Date.from_string(
                    rec.date_customer_warranty_start
                )
                end = start + delta
                rec.date_customer_warranty_end = fields.Date.to_string(end)

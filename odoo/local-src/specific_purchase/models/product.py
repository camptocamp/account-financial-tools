# -*- coding: utf-8 -*-
# Author: Denis Leemann
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_req_sn_supplier = fields.Boolean(
        string='Request SN to Supplier',
    )


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_req_sn_supplier = fields.Boolean(
        string='Request SN to Supplier',
        related='product_variant_ids.is_req_sn_supplier'
    )

    supplier_warranty = fields.Float(
        default=24.,
        help='supplier warranty duration (months)',
    )

    warranty = fields.Float(
        default=12.,
    )

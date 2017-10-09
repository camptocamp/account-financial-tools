# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo.addons.mrp.tests.test_bom import TestBoM


class TestMOFromBOM(TestBoM):

    def add_data(self):
        tmp_picking_type = self.env['stock.picking.type'].create({
            'name': 'Manufacturing',
            'code': 'mrp_operation',
            'sequence_id': self.env['ir.sequence'].search(
                [('code', '=', 'mrp.production')], limit=1).id,
        })
        self.test_bom = self.env['mrp.bom'].create({
            'product_id': self.product_7.id,
            'product_tmpl_id': self.product_7.product_tmpl_id.id,
            'product_uom_id': self.uom_unit.id,
            'product_qty': 4.0,
            'picking_type_id': tmp_picking_type.id,
            'routing_id': self.routing_2.id,
            'type': 'normal',
        })

        self.test_bom_l1 = self.env['mrp.bom.line'].create({
            'bom_id': self.test_bom.id,
            'product_id': self.product_2.id,
            'product_qty': 2,
        })

        self.test_bom_l2 = self.env['mrp.bom.line'].create({
            'bom_id': self.test_bom.id,
            'product_id': self.product_3.id,
            'product_qty': 2,
            'attribute_value_ids': [(4, self.prod_attr1_v1.id)],
        })

    def test_mo_from_bom(self):
        self.add_data()
        self.test_bom.create_manufacture_order()
        test_mo = self.env["mrp.production"].search([
            ('bom_id', '=', self.test_bom.id)
        ])
        self.assertEqual(test_mo.product_id,
                         self.test_bom.product_id)
        self.assertEqual(test_mo.product_uom_id,
                         self.test_bom.product_uom_id)
        self.assertEqual(test_mo.picking_type_id,
                         self.test_bom.picking_type_id)

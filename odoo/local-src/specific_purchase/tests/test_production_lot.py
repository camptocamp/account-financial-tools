from odoo.tests import common


class TestProductionLot(common.TransactionCase):
    def setUp(self):
        super(TestProductionLot, self).setUp()
        self.product = self.env['product.product'].create(
            {'name': 'test',
             'type': 'product',
             'tracking': 'serial',
             }
        )
        self.partner = self.env['res.partner'].create(
            {'name': 'TestPartner',
             'is_company': True,
             }
        )

    def test_create(self):
        sn = self.env['stock.production.lot'].create(
            {'name': '1234',
             'product_id': self.product.id,
             'current_partner_id': self.partner.id,
             }
        )

        # the creation of the SN has created a stock move from inventory loss
        # to customers for the prodlot
        moves = self.env['stock.move'].search(
            [('product_id', '=', self.product.id)]
        )
        self.assertEquals(len(moves), 1)
        self.assertEquals(moves.partner_id, self.partner)
        quants = self.env['stock.quant'].search(
            [('product_id', '=', self.product.id)]
        )
        self.assertEquals(len(quants), 1)
        self.assertEquals(quants.lot_id, sn)

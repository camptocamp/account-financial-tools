# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def action_export_packing_list(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/download/stockpicking/packinglist'
                   '?id=%s&filename=packlist.xlsx' % (self.id),
            'target': 'new'}

    @api.multi
    def action_export_commercial_invoice(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/download/stockpicking/commercialinvoice'
                   '?id=%s&filename=commercial_invoice.xlsx' % (self.id),
            'target': 'new'}

    @api.multi
    def get_intrastat_doc(self, document_type):
        doc_intrastat = self.env['intrastat.doc'].create(
                {'picking_id': self.id, 'document_type': document_type})
        return doc_intrastat.download()

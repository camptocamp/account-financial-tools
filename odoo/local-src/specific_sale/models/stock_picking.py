# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, exceptions, _, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    incoterm_id = fields.Many2one(
        'stock.incoterms',
        'Incoterms',
    )

    @api.multi
    def do_new_transfer(self):
        for picking in self:
            if (not picking.incoterm_id and
                    picking.picking_type_code == 'outgoing'):
                raise exceptions.UserError(_('You are trying to process '
                                             'outgoing picking without  '
                                             'incoterm'))
        return super(StockPicking, self).do_new_transfer()

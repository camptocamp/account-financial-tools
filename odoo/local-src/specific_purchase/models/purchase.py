# -*- coding: utf-8 -*-
# Author: Denis Leemann
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, exceptions, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _handle_qty_decrease(self, line, line_, sn_lst):
        """Delete lots when quantity decreased.

        :param line: purchase order line
        :param line_: line from vals
        :param sn_lst: list of serial numbers
        :return: None
        """
        self.ensure_one()
        diff = line_[2]["product_qty"] - int(
            line.product_qty)
        for sn in sn_lst[diff:]:
            self.env["stock.production.lot"].search(
                [("name", "=", sn)]
            ).unlink()
        line.req_sn_supplier = ", ".join(sn_lst[:diff])

    def _handle_qty_change(self, vals):
        """Handles the changes in quantities of products.

        creates additional lots if the quantity increased
        or deletes if the quantity decreased
        :param vals: Vals from write method. dict
        :return: dict of new vals
        """
        for line in self.env["purchase.order.line"].browse(
                [line_[1] for line_ in vals[u"order_line"]
                 if u"product_qty" in line_[2]]
        ):
            sn_lst = line.req_sn_supplier.split(", ")
            if line.product_qty > line_[2]["product_qty"]:
                self._handle_qty_decrease(line, line_, sn_lst)
            else:
                diff = line_[2]["product_qty"] - int(
                    line.product_qty)
                values = {
                    'product_id': line.product_id.id,
                }
                self._handle_qty_increase(line, values, sn_lst, diff)
        return vals

    def _handle_qty_increase(self, line, values, sn_lst, iter_value):
        """Create new lots or when quantity increases.

        :param line: purchase order line
        :param line: values for lots
        :param sn_lst: list of serial numbers
        :param iter_value: amount of lots to create
        :return: None
        """
        Lot = self.env['stock.production.lot']
        # Maybe it's suitable to change the field to
        # integer in context of this project?
        # As float is a bit weird here
        for single_lot in xrange(iter_value):
            # Was getting an error message about not
            # being able to subscribe user to the
            # same thing twice, weird
            lot = Lot.with_context(
                mail_create_nosubscribe=True
            ).create(values)
            sn_lst.append(lot.name)
        line.req_sn_supplier = ', '.join(sn_lst)

    def _handle_initial_purchase(self):
        """Handles the confirmation of purchase.order.

        Creates lots and updates req_sn_supplier field
        :return: None
        """
        self.ensure_one()
        prod_ids = self.order_line.search_read(
            [('product_id.is_req_sn_supplier', '=', True),
             ('order_id', '=', self.id)], ['product_id'])
        for prd in prod_ids:
            values = {
                'product_id': prd['product_id'][0],
            }
            line = self.order_line.search(
                [('order_id', '=', self.id),
                 ('product_id', '=', prd['product_id'][0])])
            sn_lst = []
            self._handle_qty_increase(line, values, sn_lst,
                                      int(line.product_qty))

    @api.multi
    def write(self, vals):
        for record in self:
            if 'state' in vals and vals['state'] in ('to approve', 'purchase'):
                if self.user_has_groups('purchase.group_purchase_user'):
                    if vals['state'] == 'purchase':
                        record._handle_initial_purchase()
            elif u"order_line" in vals:
                vals = record._handle_qty_change(vals)
        return super(PurchaseOrder, self).write(vals)

    @api.multi
    def button_approve(self, force=False):
        for order in self:
            for line in order.order_line:
                if not line.account_analytic_id:
                    raise exceptions.UserError(
                        _('An Analytic Account is required for Validation!'))
        return super(PurchaseOrder, self).button_approve(force=force)

    def get_requested_sn(self):
        Lot = self.env['stock.production.lot']
        prod_ids = self.order_line.search_read(
                        [('product_id.is_req_sn_supplier', '=', True),
                         ('order_id', '=', self.id)], ['product_id'])
        lot_ids = self.env['stock.production.lot']
        for prd in prod_ids:
            line = self.order_line.search(
                [('order_id', '=', self.id),
                 ('product_id', '=', prd['product_id'][0])])
            lot = Lot.search([('name', '=', line.req_sn_supplier)])
            lot_ids |= lot
        return lot_ids


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    req_sn_supplier = fields.Char(
        string='Requested SN to supplier',
    )

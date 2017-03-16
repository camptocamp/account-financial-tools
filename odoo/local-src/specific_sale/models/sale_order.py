# -*- coding: utf-8 -*-
# Author: Damien Crier
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_zone_id = fields.Many2one(comodel_name='project.zone',
                                      required=True)
    project_process_id = fields.Many2one(comodel_name='project.process',
                                         required=True)
    project_market_id = fields.Many2one(comodel_name='project.market',
                                        required=True)

    engineering_validation_id = fields.Many2one(
        'res.users',
        string='Engineering Validation',
    )
    system_validation_id = fields.Many2one(
        'res.users',
        string='System Validation',
    )
    process_validation_id = fields.Many2one(
        'res.users',
        string='Process Validation',
    )
    sales_condition = fields.Binary(
        string='Sales Condition',
        required=True,
        states={'draft': [('required', False)], }
    )
    state = fields.Selection(
        selection_add=[('final_quote', 'Final Quote')],
        default='final_quote',
    )
    filename = fields.Char()

    def _generate_acc_name(self, use_existing_one=None):
        """
        generate an analytic account name according to the following structure:
            123ABCXXYYZZ with
                123: number autoincrement (use Odoo sequence)
                ABC: customer.ref field
                XX: Code of the project zone
                YY: Code of the project process
                ZZ: Code of the project market
        """
        if use_existing_one:
            return use_existing_one

        seq = self.env['ir.sequence'].next_by_code('project')
        return ''.join([seq,
                        self.partner_id.ref or "ABC",
                        self.project_zone_id.code,
                        self.project_process_id.code,
                        self.project_market_id.code,
                        ])

    @api.multi
    def _create_analytic_account(self, prefix=None):
        super(SaleOrder, self)._create_analytic_account(prefix=prefix)
        for order in self:
            name = order._generate_acc_name()
            order.project_id.name = name

    @api.onchange('opportunity_id')
    def onchange_opportunity_id(self):
        if self.opportunity_id:
            self.update({
                'project_zone_id': self.opportunity_id.project_zone_id.id,
                'project_process_id': (
                    self.opportunity_id.project_process_id.id
                ),
                'project_market_id': self.opportunity_id.project_market_id.id,
                })

    @api.onchange('order_line', 'order_line.product_id')
    def onchange_order_line(self):
        order_line = self.order_line
        option_lines = []
        if order_line:
            for line in order_line:
                if line.product_id:
                    for product in line.product_id.optional_product_ids:
                        if self.pricelist_id:
                            price = self.pricelist_id.with_context(
                                uom=product.uom_id.id).get_product_price(
                                product, 1, False)
                        else:
                            price = product.list_price
                        data = {
                            'product_id': product.id,
                            'name': product.name,
                            'quantity': 1,
                            'uom_id': product.uom_id.id,
                            'price_unit': price,
                            'discount': 0,
                        }
                        option_lines.append((0, 0, data))
        self.options = option_lines

    def write(self, vals):
        if self.state in ('draft') and ('state' in vals and
           vals['state'] not in ('final_quote')):
            raise exceptions.UserError(
                'A Draft Sale Order can only step to "final_quote" ')
        if ('state' in vals and vals['state'] not in ('draft')):
            ghost_prd = self.order_line.search_read(
                [('product_id.is_ghost', '=', True),
                 ('order_id', '=', self.id)])
            if ghost_prd:
                raise exceptions.UserError(_(
                    'Ghost product is allowed only on draft Sale Orders'))
            if not self.sales_condition:
                raise exceptions.UserError(_(
                    'You need to attach Sales Condition'))
        return super(SaleOrder, self).write(vals)

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {}, name=_("%s (Copy)") % self.name)
        default = {
            'engineering_validation_id': False,
            'system_validation_id': False,
            'process_validation_id': False,
        }
        return super(SaleOrder, self).copy(default=default)

    def action_validate_eng(self):
        user = self.env['res.users']
        self.engineering_validation_id = user.browse(self.env.context['uid'])

    def action_validate_sys(self):
        user = self.env['res.users']
        self.system_validation_id = user.browse(self.env.context['uid'])

    def action_validate_pro(self):
        user = self.env['res.users']
        self.process_validation_id = user.browse(self.env.context['uid'])

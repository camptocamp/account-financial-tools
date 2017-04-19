# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import anthem


@anthem.log
def sales_setup(ctx):
    """ Setup sales """
    sale_settings = ctx.env['sale.config.settings']
    vals = {'group_uom': 1,
            'default_invoice_policy': 'delivery',
            'invoiced_timesheet': 'approved',
            'group_discount_per_so_line': 1,
            }
    sale_settings.create(vals).execute()


@anthem.log
def main(ctx):
    sales_setup(ctx)

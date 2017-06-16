# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem
from anthem.lyrics.records import create_or_update


@anthem.log
def create_dimensions(ctx):
    """ Create dimension and tags for analytic"""

    dim_vals = {
        'name': 'Business Unit',
        'code': 'bu',
        'analytic_tag_ids': ctx.env['account.analytic.tag'].search([]),
    }
    dim_xmlid = '__setup__.dimension_business_unit'
    create_or_update(ctx, 'account.analytic.dimension', dim_xmlid, dim_vals)

    tag_names = [('Admin', 'analytic_tag_admin'),
                 ('R&D', 'analytic_tag_rd'),
                 ('Sales & mkg', 'analytic_tag_sales_marketing'),
                 ('Composite', 'analytic_tag_composite'),
                 ('Engineering', 'analytic_tag_engineering'),
                 ('Process', 'analytic_tag_process'),
                 ('Process', 'analytic_tag_system'),
                 ]
    for tag, tag_xmlid in tag_names:
        tags_vals = {
            'name': tag,
            'analytic_dimension_id': ctx.env.ref(dim_xmlid).id,
        }
        tag_xmlid = '__setup__.%s' % tag_xmlid
        create_or_update(ctx, 'account.analytic.tag', tag_xmlid, tags_vals)


@anthem.log
def main(ctx):
    """ Main: creating account.analytic.dimensions """
    create_dimensions(ctx)

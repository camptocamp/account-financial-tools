# -*- coding: utf-8 -*-
# Author: Denis Leemann
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "RocTool Specific Purchase Module",
    "version": "10.0.1.0.0",
    "depends": [
        'purchase',
        'stock',
    ],
    "category": "Purchase",
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "website": "http://www.camptocamp.com",
    "license": "GPL-3 or any later version",
    "category": "Purchase",
    "data": [
        # security
        'security/ir.model.access.csv',
        # data
        'data/sequence.xml',
        'data/mail_message_subtypes.xml',
        # views
        'views/purchase_line_views.xml',
        'views/purchase_views.xml',
        'views/product_views.xml',
        'wizard/stock_pack_operation_views.xml',
        # reports
        'views/purchase_report.xml',
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-
# Author: Denis Leemann
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "RocTool specific Purchase Module",
    "version": "10.0.1.0.0",
    "depends": [
        'purchase',
        'hr',
    ],
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "website": "http://www.camptocamp.com",
    "license": "GPL-3 or any later version",
    "category": "Sale",
    "data": [
        # security
        'security/purchase_security.xml',
        'security/ir.model.access.csv',
        # views
        'views/purchase_views.xml',
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "RocTool intrastat documents from stock picking ",
    "version": "10.0.1.0.0",
    "description": "Allow to export 2 intrastat documents the packing-list "
                   "and the commercial-invoice in Excel format, from a "
                   "stock-picking.",
    "depends": [
        "stock",
    ],
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "website": "http://www.camptocamp.com",
    "license": "GPL-3 or any later version",
    "data": [
        'views/stock_picking.xml',
    ],
    'installable': True,
}

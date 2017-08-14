# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "RocTool specific security",
    "version": "10.0.1.0.0",
    "depends": [
        'hr_expense',
        'account',
        'hr_timesheet',
        'sale',
        'sales_team',
        'stock',
        'mrp',
        'purchase',
    ],
    "author": "Camptocamp SA",
    "website": "http://www.camptocamp.com",
    "license": "GPL-3 or any later version",
    "category": "Sale",
    "data": [
        'security/ir.model.access.csv',
    ],
    'installable': True,
}

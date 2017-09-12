# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "RocTool specific analytic module",
    "version": "10.0.1.0.0",
    "depends": [
        'sale',
        'analytic_tag_dimension',
        'purchase',
        'account',
        'hr_expense',
    ],
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "website": "http://www.camptocamp.com",
    "license": "AGPL-3",
    "category": "Analytic",
    "data": [
        'views/department_views.xml',
        'views/employee_views.xml',
        'views/purchase_order_line_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}

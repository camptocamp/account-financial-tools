# -*- coding: utf-8 -*-
# Author: Damien Crier
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "RocTool specific sale module",
    "version": "10.0.1.0.0",
    "depends": [
        'specific_crm',
        'sale',
        'sale_crm',
        'sale_margin',
        'sales_team',
        'sale_timesheet',
        'website_sale_options',
        'mrp',
        'analytic_tag_dimension',
        'analytic',
        'delivery',
    ],
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "website": "http://www.camptocamp.com",
    "license": "GPL-3 or any later version",
    "category": "Sale",
    "data": [
        'views/product_views.xml',
        'views/project_task.xml',
        'views/project_project.xml',
        'views/mrp_bom.xml',
        'views/so_mail_template.xml',
        'views/stock_picking.xml',
        'views/sale_order.xml',
        'views/sale_order_line.xml',
        'views/sale_order_crm.xml',
        'data/res_groups_data.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}

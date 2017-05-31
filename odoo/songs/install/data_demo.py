# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem
from ..common import load_csv

""" File for demo data

These songs will be called when the mode is 'demo', we should import only
excerpt of data, while the full data is only imported in the 'full' mode.

"""


@anthem.log
def import_customers(ctx):
    """ Importing customers from csv """
    load_csv(ctx, 'data/demo/customers.csv', 'res.partner')


@anthem.log
def import_products(ctx):
    """ Importing product.template from csv """
    load_csv(ctx, 'data/demo/product.template.csv', 'product.template')


def import_demo_partners(ctx):
    """ Importing partners from csv """
    load_csv(ctx, 'data/demo/demo_res_partner.csv', 'res.partner')


def import_demo_users(ctx):
    """ Importing users from csv """
    load_csv(ctx, 'data/demo/demo_res_user.csv', 'res.users')


def import_demo_hr_employee(ctx):
    """ Importing hr employee from csv """
    load_csv(ctx, 'data/demo/demo_hr_employee.csv', 'hr.employee')


@anthem.log
def main(ctx):
    """ Loading demo data """
    import_customers(ctx)
    import_products(ctx)
    import_demo_partners(ctx)
    import_demo_users(ctx)
    import_demo_hr_employee(ctx)

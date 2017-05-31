# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem
# Import temporarily the demo data for integration
from data_demo import (
    import_customers, import_products,
    import_demo_partners, import_demo_users, import_demo_hr_employee
)

""" File for full (production) data

These songs will be called on integration and production server at the
installation.

"""


@anthem.log
def main(ctx):
    """ Loading full data """
    import_customers(ctx)
    import_products(ctx)
    import_demo_partners(ctx)
    import_demo_users(ctx)
    import_demo_hr_employee(ctx)

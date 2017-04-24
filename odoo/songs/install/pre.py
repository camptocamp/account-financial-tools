# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import os

from base64 import b64encode
from pkg_resources import resource_string

import anthem

from ..common import req


@anthem.log
def setup_company(ctx):
    """ Setup company """
    # load logo on company
    logo_content = resource_string(req, 'data/images/mt-logo-b.png')
    b64_logo = b64encode(logo_content)

    values = {
        'name': "Genossenschaft Meteotest",
        'street': "Fabrikstrasse 14",
        'zip': "3012",
        'city': "Bern",
        'country_id': ctx.env.ref('base.ch').id,
        'phone': "+41 31 307 26 26",
        'fax': "+41 31 307 26 10",
        'email': "office@meteotest.ch",
        'website': "http://www.meteotest.ch",
        'vat': "CHE-108.019.245 MWST",
        'registry': 'CHE-108.019.245',
        'logo': b64_logo,
        'currency_id': ctx.env.ref('base.CHF').id,
    }
    ctx.env.ref('base.main_company').write(values)


@anthem.log
def setup_language(ctx):
    """ Installing language and configuring locale formatting """
    for code in ('fr_FR', 'de_DE'):
        ctx.env['base.language.install'].create({'lang': code}).lang_install()
    ctx.env['res.lang'].search([]).write({
        'grouping': [3, 0],
        'date_format': '%d/%m/%Y',
    })


@anthem.log
def admin_user_password(ctx):
    """ Changing admin password """
    # TODO default admin password for the test server, must be changed
    # To get an encrypted password:
    # $ docker-compose run --rm odoo python -c \
    # "from passlib.context import CryptContext; \
    #  print CryptContext(['pbkdf2_sha512']).encrypt('my_password')"
    if os.environ.get('RUNNING_ENV') == 'dev':
        ctx.log_line('Not changing password for dev RUNNING_ENV')
        return
    ctx.env.user.password_crypt = (
        '$pbkdf2-sha512$19000$CCGkVArBmFNKifHe2/u/9w$lS5JimC.iBrMxC/Abjv39'
        'IJSzJwuO1OJYY5AIx2ss1Rnz7lYK/ln0cvHaiTpA8ImGFWFDTDrso6ZpzqDLU2Gdg'
    )


@anthem.log
def main(ctx):
    """ Main: creating demo data """
    setup_company(ctx)
    setup_language(ctx)
    admin_user_password(ctx)

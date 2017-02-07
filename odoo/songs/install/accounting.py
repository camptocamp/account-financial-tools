# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem
from anthem.lyrics.records import create_or_update

from . import roctool_vars


@anthem.log
def activate_multicurrency(ctx):
    """ Activating multi-currency """
    employee_group = ctx.env.ref('base.group_user')
    employee_group.write({
        'implied_ids': [(4, ctx.env.ref('base.group_multi_currency').id)]
    })


@anthem.log
def configure_chart_of_account(ctx):
    """Configure COA for companies"""

    account_settings = ctx.env['account.config.settings']

    for company_xml_id, coa in roctool_vars.coa_dict.iteritems():
        company = ctx.env.ref(company_xml_id)
        with ctx.log("Import basic CoA for %s:" % company.name):
            vals = {'group_analytic_account_for_purchases': True,
                    'group_analytic_account_for_sales': True,
                    'group_analytic_accounting': True,
                    'module_account_tax_cash_basis': True,
                    'company_id': company.id,
                    'chart_template_id': ctx.env.ref(coa).id,
                    }
            acs = account_settings.create(vals)

            acs.onchange_chart_template_id()

            acs.execute()


@anthem.log
def configure_tax_cash_basis(ctx):
    for company in ctx.env['res.company'].search([]):
        with ctx.log("Configure Tax Cash Basis for %s:" % company.name):
            # create a 'general' journal for tax cash basis
            xml_id = '__setup__.tax_cash_basis_%s' % company.id
            record = {
                'name': 'Tax Cash basis',
                'type': 'general',
                'code': 'TCB',
                'company_id': company.id
            }
            create_or_update(ctx, 'account.journal', xml_id, record)

            tcb = ctx.env.ref(xml_id)
            # configure tax cash basis on companies
            vals = {'module_account_tax_cash_basis': True,
                    'tax_cash_basis_journal_id': tcb.id,
                    'company_id': company.id,
                    }
            acs = ctx.env['account.config.settings'].create(vals)

            acs.execute()


@anthem.log
def create_bank_accounts(ctx):
    """ Creating bank accounts """
    expense_type = ctx.env.ref('account.data_account_type_expenses')
    records = [
        {'xmlid': '__setup__.account_1010',
         'name': 'XXX 00-001285-1',
         'code': '991010',
         'user_type_id': expense_type.id,
         },
        {'xmlid': '__setup__.account_1020',
         'name': 'ZZZ BE7400700115500080000',
         'code': '991020',
         'user_type_id': expense_type.id,
         },
        {'xmlid': '__setup__.account_1021',
         'name': 'ZZZ BE2300700115500172222',
         'code': '991021',
         'user_type_id': expense_type.id,
         },
    ]
    for record in records:
        xmlid = record.pop('xmlid')
        create_or_update(ctx, 'account.account', xmlid, record)


@anthem.log
def main(ctx):
    """ Configuring accounting """
    activate_multicurrency(ctx)
    create_bank_accounts(ctx)

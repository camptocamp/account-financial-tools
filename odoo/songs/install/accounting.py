# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem
from anthem.lyrics.records import add_xmlid
from ..common import load_csv


@anthem.log
def activate_multicurrency(ctx):
    """ Activating multi-currency """
    employee_group = ctx.env.ref('base.group_user')
    employee_group.write({
        'implied_ids': [(4, ctx.env.ref('base.group_multi_currency').id)]
    })


def import_coa(ctx, coa):
    TaxTemplate = ctx.env['account.tax.template']
    sale_tax = TaxTemplate.search(
        [('chart_template_id', 'parent_of', coa.id),
         ('type_tax_use', '=', 'sale')], limit=1,
        order="sequence, id desc")
    purchase_tax = TaxTemplate.search(
        [('chart_template_id', 'parent_of', coa.id),
         ('type_tax_use', '=', 'purchase')], limit=1,
        order="sequence, id desc")
    wizard = ctx.env['wizard.multi.charts.accounts'].create({
        'company_id': ctx.env.user.company_id.id,
        'chart_template_id': coa.id,
        'transfer_account_id': coa.transfer_account_id.id,
        'code_digits': 4,
        'sale_tax_id': sale_tax.id,
        'purchase_tax_id': purchase_tax.id,
        'sale_tax_rate': 15,
        'purchase_tax_rate': 15,
        'complete_tax_set': coa.complete_tax_set,
        'currency_id': ctx.env.ref('base.CHF').id,
        'bank_account_code_prefix': coa.bank_account_code_prefix,
        'cash_account_code_prefix': coa.cash_account_code_prefix,
    })
    wizard.execute()


@anthem.log
def add_xmlid_account(ctx):
    accounts = ctx.env['account.account'].search([])
    for account in accounts:
        add_xmlid(
            ctx, account,
            '__setup__.account_account_meteotest_%s' % account.code,
            noupdate=True
        )


@anthem.log
def add_xmlid_journal(ctx):
    journals = ctx.env['account.journal'].search([])
    for journal in journals:
        journal_code = journal.code
        add_xmlid(
            ctx, journal, '__setup__.account_journal_meteotest_%s' %
                          (journal_code.lower()), noupdate=True)


@anthem.log
def load_account(ctx):
    """ Setup CoA """
    with ctx.log("Import basic CoA"):
        coa = ctx.env.ref('l10n_ch.l10nch_chart_template')
        coa.digits = 4
        import_coa(ctx, coa)
        add_xmlid_account(ctx)


@anthem.log
def process_coa_translations(ctx):
    """ Translate accounts and taxes """
    chart_template = ctx.env.ref('l10n_ch.l10nch_chart_template')
    chart_template.process_coa_translations()


@anthem.log
def update_coa(ctx):
    """ Load CSV to override basic accounts """
    # Change user lang to german to update account names in german

    # Setup user lang and context
    lang_origin = ctx.env.user.lang
    ctx_origin = ctx.env.context
    ctx_lang = ctx_origin.copy()
    ctx_lang['lang'] = 'de_DE'
    ctx.env.user.lang = 'de_DE'
    ctx.env.context = ctx_lang
    ctx.env.args = ctx.env.cr, ctx.env.uid, ctx.env.context

    load_csv(ctx, 'data/install/account.account.csv', 'account.account')

    # rollback lang
    ctx.env.user.lang = lang_origin
    ctx.env.context = ctx_origin
    ctx.env.args = ctx.env.cr, ctx.env.uid, ctx.env.context


@anthem.log
def main(ctx):
    """ Configuring accounting """
    activate_multicurrency(ctx)
    load_account(ctx)
    process_coa_translations(ctx)
    update_coa(ctx)
    add_xmlid_journal(ctx)

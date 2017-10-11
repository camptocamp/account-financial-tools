# -*- coding: utf-8 -*-
# Copyright  Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
# -- This file has been generated --

import anthem
from ...common import load_csv


@anthem.log
def load_account_account_tag(ctx):
    """ Import account.account.tag from csv """
    model = ctx.env['account.account.tag'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.account.tag.csv', model)


@anthem.log
def load_res_currency(ctx):
    """ Import res.currency from csv """
    model = ctx.env['res.currency'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/res.currency.csv', model)


@anthem.log
def load_account_financial_html_report_line(ctx):
    """ Import account.financial.html.report.line from csv """
    model = ctx.env['account.financial.html.report.line'].with_context({'tracking_disable':1})  # noqa
    header_exclude = ['children_ids/id', 'parent_id/id']
    load_csv(ctx, 'data/install/generated/account.financial.html.report.line.csv', model, header_exclude=header_exclude)  # noqa
    if header_exclude:
        load_csv(ctx, 'data/install/generated/account.financial.html.report.line.csv', model, header=['id', ] + header_exclude)  # noqa


@anthem.log
def load_account_financial_html_report(ctx):
    """ Import account.financial.html.report from csv """
    model = ctx.env['account.financial.html.report'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.financial.html.report.csv', model)


@anthem.log
def load_product_category(ctx):
    """ Import product.category from csv """
    model = ctx.env['product.category'].with_context({'tracking_disable':1})  # noqa
    header_exclude = ['parent_id/id']
    load_csv(ctx, 'data/install/generated/product.category.csv', model, header_exclude=header_exclude)  # noqa
    if header_exclude:
        load_csv(ctx, 'data/install/generated/product.category.csv', model, header=['id', ] + header_exclude)  # noqa


@anthem.log
def load_account_fiscal_position_tax(ctx):
    """ Import account.fiscal.position.tax from csv """
    model = ctx.env['account.fiscal.position.tax'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.fiscal.position.tax.csv', model)


@anthem.log
def load_res_bank(ctx):
    """ Import res.bank from csv """
    model = ctx.env['res.bank'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/res.bank.csv', model)


@anthem.log
def add_xmlid_to_existing_ir_sequence(ctx):
    # this works if `base_dj` is installed
    model = ctx.env['ir.sequence'].with_context(
        dj_xmlid_fields_map={'ir.sequence': [] },
        dj_multicompany=True,
    )
    for item in model.search([]):
        item._dj_export_xmlid()


@anthem.log
def load_account_account_type(ctx):
    """ Import account.account.type from csv """
    model = ctx.env['account.account.type'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.account.type.csv', model)


@anthem.log
def load_account_account(ctx):
    """ Import account.account from csv """
    model = ctx.env['account.account'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.account.csv', model)


@anthem.log
def load_ir_sequence(ctx):
    """ Import ir.sequence from csv """
    model = ctx.env['ir.sequence'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/ir.sequence-account.csv', model)


@anthem.log
def load_account_journal(ctx):
    """ Import account.journal from csv """
    model = ctx.env['account.journal'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.journal.csv', model)


@anthem.log
def load_account_analytic_account(ctx):
    """ Import account.analytic.account from csv """
    model = ctx.env['account.analytic.account'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.analytic.account.csv', model)


@anthem.log
def load_account_tax(ctx):
    """ Import account.tax from csv """
    model = ctx.env['account.tax'].with_context({'tracking_disable':1})  # noqa
    header_exclude = ['children_tax_ids/id']
    load_csv(ctx, 'data/install/generated/account.tax.csv', model, header_exclude=header_exclude)  # noqa
    if header_exclude:
        load_csv(ctx, 'data/install/generated/account.tax.csv', model, header=['id', ] + header_exclude)  # noqa


@anthem.log
def load_ir_property(ctx):
    """ Import ir.property from csv """
    model = ctx.env['ir.property'].with_context({'tracking_disable':1, 'xmlid_value_reference': True})  # noqa
    load_csv(ctx, 'data/install/generated/ir.property-account.csv', model)



@anthem.log
def account_config_settings_CN(ctx):
    """ Setup account.config.settings for Roctool China """
    model = ctx.env['account.config.settings'].with_context({'tracking_disable':1})
    model.create({
        # Date de verrouillage  # noqa
        'fiscalyear_lock_date': False,
        # Préfixe du compte banque *  # noqa
        'bank_account_code_prefix': False,
        # Préfixe des Comptes de Caisse *  # noqa
        'cash_account_code_prefix': False,
        # Gestion d'actifs  # noqa
        'module_account_asset': False,
        # SEPA Pain Version *: Générique  # noqa
        'sepa_pain_version': 'pain.001.001.03',
        # Devise par défaut  # noqa
        'currency_id': ctx.env.ref('base.CNY').id,
        # Fonctions de comptabilité complète: journaux, déclarations légales, plan comptable, etc.  # noqa
        'module_account_accountant': True,
        # Dernier jour de l'exercice fiscal  # noqa
        'fiscalyear_last_day': 31,
        # Nombres de jours entre deux relances  # noqa
        'days_between_two_followups': 14,
        # Cette société a son propre plan comptable  # noqa
        'expects_chart_of_accounts': True,
        # Connecteur Plaid  # noqa
        'module_account_plaid': False,
        # Ensemble complet de taxes  # noqa
        'complete_tax_set': False,
        # ID du modèle de compte de transfert  # noqa
        'template_transfer_account_id': False,
        # Utilisez les paiements SEPA  # noqa
        'module_account_sepa': True,
        # Importer au format .csv  # noqa
        'module_account_bank_statement_import_csv': False,
        # Gestion du budget  # noqa
        'module_account_budget': False,
        # Société  # noqa
        'company_id': ctx.env.ref('__setup__.roctool_china').id,
        # Comptabilité analytique pour les ventes  # noqa
        'group_analytic_account_for_sales': True,
        # Avertissement: Tous les partenaires peuvent être utilisés dans les factures  # noqa
        'group_warning_account': False,
        # Expense Journal  # noqa
        # 'expense_journal_id': ctx.env.ref('__setup__.account_journal_expense_roctool_china').id,
        # Autoriser devises multiples  # noqa
        'group_multi_currency': True,
        # Autoriser les factures proforma  # noqa
        'group_proforma_invoices': False,
        # Reconnaissance des revenus  # noqa
        'module_account_deferred_revenue': False,
        # Obtenez des rapports comptables dynamiques  # noqa
        'module_account_reports': True,
        # La société a un plan comptable  # noqa
        'has_chart_of_accounts': False,
        # A une société par défaut  # noqa
        'has_default_company': False,
        # Compute sales tax automatically in the United States using TaxCloud.  # noqa
        'module_account_taxcloud': False,
        # Nom de votre société *  # noqa
        'sepa_initiating_party_name': "RocTool SA",
        # Taxe d'achat (%)  # noqa
        'purchase_tax_rate': 0.0,
        # Unité de l'intervalle: Manuellement  # noqa
        'currency_interval_unit': 'manually',
        # Importer au format .ofx  # noqa
        'module_account_bank_statement_import_ofx': True,
        # Activer l'impression et le dépôt de chèques   # noqa
        'module_l10n_us_check_printing': False,
        # Taxe d'achat par défaut  # noqa
        'default_purchase_tax_id': False,
        # Fournisseur du service: Banque centrale européenne  # noqa
        'currency_provider': 'ecb',
        # Identification *  # noqa
        'sepa_orgid_id': False,
        # Journal pour taxes sur base des paiements  # noqa
        # 'tax_cash_basis_journal_id': False,
        # Utiliser la comptabilité anglo-saxonne  # noqa
        'use_anglo_saxon': False,
        # Taxe de vente (%)  # noqa
        'sale_tax_rate': 0.0,
        # Utiliser dépôt de lot  # noqa
        'module_account_batch_deposit': False,
        # Interface bancaire - Synchronisez vos flux bancaires automatiquement  # noqa
        'module_account_yodlee': True,
        # Permettre les taxes sur les paiements  # noqa
        'module_account_tax_cash_basis': True,
        # Nombre de chiffres *  # noqa
        'code_digits': 0,
        # Activer la gestion des relances de paiement  # noqa
        'module_account_reports_followup': False,
        # Modèle  # noqa
        'chart_template_id': False,
        # Taxe de vente par défaut  # noqa
        'default_sale_tax_id': False,
        # Message des Paiements en retard *  # noqa
        'overdue_msg': """Dear Sir/Madam,

Our records indicate that some payments on your account are still due. Please find details below.
If the amount has already been paid, please disregard this notice. Otherwise, please forward us the total amount stated below.
If you have any queries regarding your account, Please contact us.

Thank you in advance for your cooperation.
Best Regards,""",
        # Taxe de vente par défaut  # noqa
        'sale_tax_id': False,
        # Journal des différences de taux  # noqa
        'currency_exchange_journal_id': False,
        # Importer des fichiers .qif  # noqa
        'module_account_bank_statement_import_qif': False,
        # Compte analytique  # noqa
        'group_analytic_accounting': True,
        # Prochaine date d'exécution  # noqa
        'currency_next_execution_date': False,
        # Comptabilité analytique pour les achats  # noqa
        'group_analytic_account_for_purchases': True,
        # Date de verrouillage pour les non-conseillers  # noqa
        'period_lock_date': False,
        # Aperçu des comptes bancaires en pied de page  # noqa
        'company_footer': """False""",
        # Émetteur *  # noqa
        'sepa_orgid_issr': False,
        # Dernier mois de l'exercice: décembre  # noqa
        'fiscalyear_last_month': 12,
        # Méthode d'arrondissement des Taxes *: Arrondir à la ligne  # noqa
        'tax_calculation_rounding_method': 'round_per_line',
        # Acquéreur par défaut   # noqa
        'default_acquirer': False,
        # Taxe d'achat par défaut  # noqa
        'purchase_tax_id': False,
        # Users Receiving the Intrastat Reminder  # noqa
        'intrastat_remind_user_ids': [],
        # Compte de transfert inter-bancaire  # noqa
        'transfer_account_id': False,
        
    }).execute()

@anthem.log
def account_config_settings_DE(ctx):
    """ Setup account.config.settings for RocTool GmbH """
    model = ctx.env['account.config.settings'].with_context({'tracking_disable':1})
    model.create({
        # Date de verrouillage  # noqa
        'fiscalyear_lock_date': False,
        # Préfixe du compte banque *  # noqa
        'bank_account_code_prefix': 1200,
        # Préfixe des Comptes de Caisse *  # noqa
        'cash_account_code_prefix': 1000,
        # Gestion d'actifs  # noqa
        'module_account_asset': False,
        # SEPA Pain Version *: Générique  # noqa
        'sepa_pain_version': 'pain.001.001.03',
        # Devise par défaut  # noqa
        'currency_id': ctx.env.ref('base.EUR').id,
        # Fonctions de comptabilité complète: journaux, déclarations légales, plan comptable, etc.  # noqa
        'module_account_accountant': True,
        # Dernier jour de l'exercice fiscal  # noqa
        'fiscalyear_last_day': 31,
        # Nombres de jours entre deux relances  # noqa
        'days_between_two_followups': 14,
        # Cette société a son propre plan comptable  # noqa
        'expects_chart_of_accounts': True,
        # Connecteur Plaid  # noqa
        'module_account_plaid': False,
        # Ensemble complet de taxes  # noqa
        'complete_tax_set': False,
        # ID du modèle de compte de transfert  # noqa
        'template_transfer_account_id': False,
        # Utilisez les paiements SEPA  # noqa
        'module_account_sepa': True,
        # Importer au format .csv  # noqa
        'module_account_bank_statement_import_csv': False,
        # Gestion du budget  # noqa
        'module_account_budget': False,
        # Société  # noqa
        'company_id': ctx.env.ref('__setup__.roctool_gmbh').id,
        # Comptabilité analytique pour les ventes  # noqa
        'group_analytic_account_for_sales': True,
        # Avertissement: Tous les partenaires peuvent être utilisés dans les factures  # noqa
        'group_warning_account': False,
        # Expense Journal  # noqa
        # 'expense_journal_id': ctx.env.ref('__setup__.account_journal_expense_roctool_gmbh').id,
        # Autoriser devises multiples  # noqa
        'group_multi_currency': True,
        # Autoriser les factures proforma  # noqa
        'group_proforma_invoices': False,
        # Reconnaissance des revenus  # noqa
        'module_account_deferred_revenue': False,
        # Obtenez des rapports comptables dynamiques  # noqa
        'module_account_reports': True,
        # La société a un plan comptable  # noqa
        'has_chart_of_accounts': False,
        # A une société par défaut  # noqa
        'has_default_company': False,
        # Compute sales tax automatically in the United States using TaxCloud.  # noqa
        'module_account_taxcloud': False,
        # Nom de votre société *  # noqa
        'sepa_initiating_party_name': "RocTool SA",
        # Taxe d'achat (%)  # noqa
        'purchase_tax_rate': 0.0,
        # Unité de l'intervalle: Manuellement  # noqa
        'currency_interval_unit': 'manually',
        # Importer au format .ofx  # noqa
        'module_account_bank_statement_import_ofx': True,
        # Activer l'impression et le dépôt de chèques   # noqa
        'module_l10n_us_check_printing': False,
        # Taxe d'achat par défaut  # noqa
        'default_purchase_tax_id': False,
        # Fournisseur du service: Banque centrale européenne  # noqa
        'currency_provider': 'ecb',
        # Identification *  # noqa
        'sepa_orgid_id': False,
        # Journal pour taxes sur base des paiements  # noqa
        # 'tax_cash_basis_journal_id': ctx.env.ref('__setup__.account_journal_tax_cash_basis').id,
        # Utiliser la comptabilité anglo-saxonne  # noqa
        'use_anglo_saxon': False,
        # Taxe de vente (%)  # noqa
        'sale_tax_rate': 0.0,
        # Utiliser dépôt de lot  # noqa
        'module_account_batch_deposit': False,
        # Interface bancaire - Synchronisez vos flux bancaires automatiquement  # noqa
        'module_account_yodlee': True,
        # Permettre les taxes sur les paiements  # noqa
        'module_account_tax_cash_basis': True,
        # Nombre de chiffres *  # noqa
        'code_digits': 6,
        # Activer la gestion des relances de paiement  # noqa
        'module_account_reports_followup': False,
        # Modèle  # noqa
        'chart_template_id': False,
        # Taxe de vente par défaut  # noqa
        'default_sale_tax_id': False,
        # Message des Paiements en retard *  # noqa
        'overdue_msg': """Dear Sir/Madam,

Our records indicate that some payments on your account are still due. Please find details below.
If the amount has already been paid, please disregard this notice. Otherwise, please forward us the total amount stated below.
If you have any queries regarding your account, Please contact us.

Thank you in advance for your cooperation.
Best Regards,""",
        # Taxe de vente par défaut  # noqa
        'sale_tax_id': False,
        # Journal des différences de taux  # noqa
        #'currency_exchange_journal_id': ctx.env.ref('__setup__.account_journal_exchange_difference').id,
        # Importer des fichiers .qif  # noqa
        'module_account_bank_statement_import_qif': False,
        # Compte analytique  # noqa
        'group_analytic_accounting': True,
        # Prochaine date d'exécution  # noqa
        'currency_next_execution_date': False,
        # Comptabilité analytique pour les achats  # noqa
        'group_analytic_account_for_purchases': True,
        # Date de verrouillage pour les non-conseillers  # noqa
        'period_lock_date': False,
        # Aperçu des comptes bancaires en pied de page  # noqa
        'company_footer': """False""",
        # Émetteur *  # noqa
        'sepa_orgid_issr': False,
        # Dernier mois de l'exercice: décembre  # noqa
        'fiscalyear_last_month': 12,
        # Méthode d'arrondissement des Taxes *: Arrondir à la ligne  # noqa
        'tax_calculation_rounding_method': 'round_per_line',
        # Acquéreur par défaut   # noqa
        'default_acquirer': False,
        # Taxe d'achat par défaut  # noqa
        'purchase_tax_id': False,
        # Users Receiving the Intrastat Reminder  # noqa
        'intrastat_remind_user_ids': [],
        # Compte de transfert inter-bancaire  # noqa
        #'transfer_account_id': ctx.env.ref('l10n_de_skr03.5_account_1327').id,
        
    }).execute()

@anthem.log
def account_config_settings_HLD(ctx):
    """ Setup account.config.settings for RocTool Holding """
    model = ctx.env['account.config.settings'].with_context({'tracking_disable':1})
    model.create({
        # Date de verrouillage  # noqa
        'fiscalyear_lock_date': False,
        # Préfixe du compte banque *  # noqa
        'bank_account_code_prefix': False,
        # Préfixe des Comptes de Caisse *  # noqa
        'cash_account_code_prefix': False,
        # Gestion d'actifs  # noqa
        'module_account_asset': False,
        # SEPA Pain Version *: Générique  # noqa
        'sepa_pain_version': 'pain.001.001.03',
        # Devise par défaut  # noqa
        'currency_id': ctx.env.ref('base.EUR').id,
        # Fonctions de comptabilité complète: journaux, déclarations légales, plan comptable, etc.  # noqa
        'module_account_accountant': True,
        # Dernier jour de l'exercice fiscal  # noqa
        'fiscalyear_last_day': 31,
        # Nombres de jours entre deux relances  # noqa
        'days_between_two_followups': 14,
        # Cette société a son propre plan comptable  # noqa
        'expects_chart_of_accounts': True,
        # Connecteur Plaid  # noqa
        'module_account_plaid': False,
        # Ensemble complet de taxes  # noqa
        'complete_tax_set': False,
        # ID du modèle de compte de transfert  # noqa
        'template_transfer_account_id': False,
        # Utilisez les paiements SEPA  # noqa
        'module_account_sepa': True,
        # Importer au format .csv  # noqa
        'module_account_bank_statement_import_csv': False,
        # Gestion du budget  # noqa
        'module_account_budget': False,
        # Société  # noqa
        'company_id': ctx.env.ref('__setup__.roctool_holding').id,
        # Comptabilité analytique pour les ventes  # noqa
        'group_analytic_account_for_sales': True,
        # Avertissement: Tous les partenaires peuvent être utilisés dans les factures  # noqa
        'group_warning_account': False,
        # Expense Journal  # noqa
        # 'expense_journal_id': ctx.env.ref('__setup__.account_journal_expense_roctool_holding').id,
        # Autoriser devises multiples  # noqa
        'group_multi_currency': True,
        # Autoriser les factures proforma  # noqa
        'group_proforma_invoices': False,
        # Reconnaissance des revenus  # noqa
        'module_account_deferred_revenue': False,
        # Obtenez des rapports comptables dynamiques  # noqa
        'module_account_reports': True,
        # La société a un plan comptable  # noqa
        'has_chart_of_accounts': False,
        # A une société par défaut  # noqa
        'has_default_company': False,
        # Compute sales tax automatically in the United States using TaxCloud.  # noqa
        'module_account_taxcloud': False,
        # Nom de votre société *  # noqa
        'sepa_initiating_party_name': "Roctool",
        # Taxe d'achat (%)  # noqa
        'purchase_tax_rate': 0.0,
        # Unité de l'intervalle: Manuellement  # noqa
        'currency_interval_unit': 'manually',
        # Importer au format .ofx  # noqa
        'module_account_bank_statement_import_ofx': True,
        # Activer l'impression et le dépôt de chèques   # noqa
        'module_l10n_us_check_printing': False,
        # Taxe d'achat par défaut  # noqa
        'default_purchase_tax_id': False,
        # Fournisseur du service: Banque centrale européenne  # noqa
        'currency_provider': 'ecb',
        # Identification *  # noqa
        'sepa_orgid_id': False,
        # Journal pour taxes sur base des paiements  # noqa
        # 'tax_cash_basis_journal_id': ctx.env.ref('__setup__.account_journal_tax_cash_basis_21').id,
        # Utiliser la comptabilité anglo-saxonne  # noqa
        'use_anglo_saxon': False,
        # Taxe de vente (%)  # noqa
        'sale_tax_rate': 0.0,
        # Utiliser dépôt de lot  # noqa
        'module_account_batch_deposit': False,
        # Interface bancaire - Synchronisez vos flux bancaires automatiquement  # noqa
        'module_account_yodlee': True,
        # Permettre les taxes sur les paiements  # noqa
        'module_account_tax_cash_basis': True,
        # Nombre de chiffres *  # noqa
        'code_digits': 0,
        # Activer la gestion des relances de paiement  # noqa
        'module_account_reports_followup': False,
        # Modèle  # noqa
        'chart_template_id': False,
        # Taxe de vente par défaut  # noqa
        'default_sale_tax_id': False,
        # Message des Paiements en retard *  # noqa
        'overdue_msg': """Dear Sir/Madam,

Our records indicate that some payments on your account are still due. Please find details below.
If the amount has already been paid, please disregard this notice. Otherwise, please forward us the total amount stated below.
If you have any queries regarding your account, Please contact us.

Thank you in advance for your cooperation.
Best Regards,""",
        # Taxe de vente par défaut  # noqa
        'sale_tax_id': False,
        # Journal des différences de taux  # noqa
        'currency_exchange_journal_id': False,
        # Importer des fichiers .qif  # noqa
        'module_account_bank_statement_import_qif': False,
        # Compte analytique  # noqa
        'group_analytic_accounting': True,
        # Prochaine date d'exécution  # noqa
        'currency_next_execution_date': False,
        # Comptabilité analytique pour les achats  # noqa
        'group_analytic_account_for_purchases': True,
        # Date de verrouillage pour les non-conseillers  # noqa
        'period_lock_date': False,
        # Aperçu des comptes bancaires en pied de page  # noqa
        'company_footer': """False""",
        # Émetteur *  # noqa
        'sepa_orgid_issr': False,
        # Dernier mois de l'exercice: décembre  # noqa
        'fiscalyear_last_month': 12,
        # Méthode d'arrondissement des Taxes *: Arrondir à la ligne  # noqa
        'tax_calculation_rounding_method': 'round_per_line',
        # Acquéreur par défaut   # noqa
        'default_acquirer': False,
        # Taxe d'achat par défaut  # noqa
        'purchase_tax_id': False,
        # Users Receiving the Intrastat Reminder  # noqa
        'intrastat_remind_user_ids': [],
        # Compte de transfert inter-bancaire  # noqa
        'transfer_account_id': False,
        
    }).execute()

@anthem.log
def account_config_settings_US(ctx):
    """ Setup account.config.settings for RocTool Inc. """
    model = ctx.env['account.config.settings'].with_context({'tracking_disable':1})
    model.create({
        # Date de verrouillage  # noqa
        'fiscalyear_lock_date': False,
        # Préfixe du compte banque *  # noqa
        'bank_account_code_prefix': 1014,
        # Préfixe des Comptes de Caisse *  # noqa
        'cash_account_code_prefix': 1015,
        # Gestion d'actifs  # noqa
        'module_account_asset': False,
        # SEPA Pain Version *: Générique  # noqa
        'sepa_pain_version': 'pain.001.001.03',
        # Devise par défaut  # noqa
        'currency_id': ctx.env.ref('base.USD').id,
        # Fonctions de comptabilité complète: journaux, déclarations légales, plan comptable, etc.  # noqa
        'module_account_accountant': True,
        # Dernier jour de l'exercice fiscal  # noqa
        'fiscalyear_last_day': 31,
        # Nombres de jours entre deux relances  # noqa
        'days_between_two_followups': 14,
        # Cette société a son propre plan comptable  # noqa
        'expects_chart_of_accounts': True,
        # Connecteur Plaid  # noqa
        'module_account_plaid': False,
        # Ensemble complet de taxes  # noqa
        'complete_tax_set': False,
        # ID du modèle de compte de transfert  # noqa
        'template_transfer_account_id': False,
        # Utilisez les paiements SEPA  # noqa
        'module_account_sepa': True,
        # Importer au format .csv  # noqa
        'module_account_bank_statement_import_csv': False,
        # Gestion du budget  # noqa
        'module_account_budget': False,
        # Société  # noqa
        'company_id': ctx.env.ref('__setup__.roctool_inc').id,
        # Comptabilité analytique pour les ventes  # noqa
        'group_analytic_account_for_sales': True,
        # Avertissement: Tous les partenaires peuvent être utilisés dans les factures  # noqa
        'group_warning_account': False,
        # Expense Journal  # noqa
        # 'expense_journal_id': ctx.env.ref('__setup__.account_journal_expense_roctool_inc').id,
        # Autoriser devises multiples  # noqa
        'group_multi_currency': True,
        # Autoriser les factures proforma  # noqa
        'group_proforma_invoices': False,
        # Reconnaissance des revenus  # noqa
        'module_account_deferred_revenue': False,
        # Obtenez des rapports comptables dynamiques  # noqa
        'module_account_reports': True,
        # La société a un plan comptable  # noqa
        'has_chart_of_accounts': False,
        # A une société par défaut  # noqa
        'has_default_company': False,
        # Compute sales tax automatically in the United States using TaxCloud.  # noqa
        'module_account_taxcloud': False,
        # Nom de votre société *  # noqa
        'sepa_initiating_party_name': "RocTool SA",
        # Taxe d'achat (%)  # noqa
        'purchase_tax_rate': 0.0,
        # Unité de l'intervalle: Manuellement  # noqa
        'currency_interval_unit': 'manually',
        # Importer au format .ofx  # noqa
        'module_account_bank_statement_import_ofx': True,
        # Activer l'impression et le dépôt de chèques   # noqa
        'module_l10n_us_check_printing': False,
        # Taxe d'achat par défaut  # noqa
        'default_purchase_tax_id': False,
        # Fournisseur du service: Banque centrale européenne  # noqa
        'currency_provider': 'ecb',
        # Identification *  # noqa
        'sepa_orgid_id': False,
        # Journal pour taxes sur base des paiements  # noqa
        # 'tax_cash_basis_journal_id': ctx.env.ref('__setup__.account_journal_tax_cash_basis_22').id,
        # Utiliser la comptabilité anglo-saxonne  # noqa
        'use_anglo_saxon': True,
        # Taxe de vente (%)  # noqa
        'sale_tax_rate': 0.0,
        # Utiliser dépôt de lot  # noqa
        'module_account_batch_deposit': False,
        # Interface bancaire - Synchronisez vos flux bancaires automatiquement  # noqa
        'module_account_yodlee': True,
        # Permettre les taxes sur les paiements  # noqa
        'module_account_tax_cash_basis': True,
        # Nombre de chiffres *  # noqa
        'code_digits': 6,
        # Activer la gestion des relances de paiement  # noqa
        'module_account_reports_followup': False,
        # Modèle  # noqa
        'chart_template_id': False,
        # Taxe de vente par défaut  # noqa
        'default_sale_tax_id': False,
        # Message des Paiements en retard *  # noqa
        'overdue_msg': """Dear Sir/Madam,

Our records indicate that some payments on your account are still due. Please find details below.
If the amount has already been paid, please disregard this notice. Otherwise, please forward us the total amount stated below.
If you have any queries regarding your account, Please contact us.

Thank you in advance for your cooperation.
Best Regards,""",
        # Taxe de vente par défaut  # noqa
        'sale_tax_id': False,
        # Journal des différences de taux  # noqa
        #'currency_exchange_journal_id': ctx.env.ref('__setup__.account_journal_exchange_difference_13').id,
        # Importer des fichiers .qif  # noqa
        'module_account_bank_statement_import_qif': False,
        # Compte analytique  # noqa
        'group_analytic_accounting': True,
        # Prochaine date d'exécution  # noqa
        'currency_next_execution_date': False,
        # Comptabilité analytique pour les achats  # noqa
        'group_analytic_account_for_purchases': True,
        # Date de verrouillage pour les non-conseillers  # noqa
        'period_lock_date': False,
        # Aperçu des comptes bancaires en pied de page  # noqa
        'company_footer': """False""",
        # Émetteur *  # noqa
        'sepa_orgid_issr': False,
        # Dernier mois de l'exercice: décembre  # noqa
        'fiscalyear_last_month': 12,
        # Méthode d'arrondissement des Taxes *: Arrondir à la ligne  # noqa
        'tax_calculation_rounding_method': 'round_per_line',
        # Acquéreur par défaut   # noqa
        'default_acquirer': False,
        # Taxe d'achat par défaut  # noqa
        'purchase_tax_id': False,
        # Users Receiving the Intrastat Reminder  # noqa
        'intrastat_remind_user_ids': [],
        # Compte de transfert inter-bancaire  # noqa
        #'transfer_account_id': ctx.env.ref('l10n_generic_coa.4_transfer_account_id').id,
        
    }).execute()

@anthem.log
def account_config_settings_JP(ctx):
    """ Setup account.config.settings for RocTool Japan """
    model = ctx.env['account.config.settings'].with_context({'tracking_disable':1})
    model.create({
        # Date de verrouillage  # noqa
        'fiscalyear_lock_date': False,
        # Préfixe du compte banque *  # noqa
        'bank_account_code_prefix': 'A11102',
        # Préfixe des Comptes de Caisse *  # noqa
        'cash_account_code_prefix': 'A11105',
        # Gestion d'actifs  # noqa
        'module_account_asset': False,
        # SEPA Pain Version *: Générique  # noqa
        'sepa_pain_version': 'pain.001.001.03',
        # Devise par défaut  # noqa
        'currency_id': ctx.env.ref('base.JPY').id,
        # Fonctions de comptabilité complète: journaux, déclarations légales, plan comptable, etc.  # noqa
        'module_account_accountant': True,
        # Dernier jour de l'exercice fiscal  # noqa
        'fiscalyear_last_day': 31,
        # Nombres de jours entre deux relances  # noqa
        'days_between_two_followups': 14,
        # Cette société a son propre plan comptable  # noqa
        'expects_chart_of_accounts': True,
        # Connecteur Plaid  # noqa
        'module_account_plaid': False,
        # Ensemble complet de taxes  # noqa
        'complete_tax_set': False,
        # ID du modèle de compte de transfert  # noqa
        'template_transfer_account_id': False,
        # Utilisez les paiements SEPA  # noqa
        'module_account_sepa': True,
        # Importer au format .csv  # noqa
        'module_account_bank_statement_import_csv': False,
        # Gestion du budget  # noqa
        'module_account_budget': False,
        # Société  # noqa
        'company_id': ctx.env.ref('__setup__.roctool_japan').id,
        # Comptabilité analytique pour les ventes  # noqa
        'group_analytic_account_for_sales': True,
        # Avertissement: Tous les partenaires peuvent être utilisés dans les factures  # noqa
        'group_warning_account': False,
        # Expense Journal  # noqa
        # 'expense_journal_id': ctx.env.ref('__setup__.account_journal_expense_roctool_japan').id,
        # Autoriser devises multiples  # noqa
        'group_multi_currency': True,
        # Autoriser les factures proforma  # noqa
        'group_proforma_invoices': False,
        # Reconnaissance des revenus  # noqa
        'module_account_deferred_revenue': False,
        # Obtenez des rapports comptables dynamiques  # noqa
        'module_account_reports': True,
        # La société a un plan comptable  # noqa
        'has_chart_of_accounts': False,
        # A une société par défaut  # noqa
        'has_default_company': False,
        # Compute sales tax automatically in the United States using TaxCloud.  # noqa
        'module_account_taxcloud': False,
        # Nom de votre société *  # noqa
        'sepa_initiating_party_name': "RocTool SA",
        # Taxe d'achat (%)  # noqa
        'purchase_tax_rate': 0.0,
        # Unité de l'intervalle: Manuellement  # noqa
        'currency_interval_unit': 'manually',
        # Importer au format .ofx  # noqa
        'module_account_bank_statement_import_ofx': True,
        # Activer l'impression et le dépôt de chèques   # noqa
        'module_l10n_us_check_printing': False,
        # Taxe d'achat par défaut  # noqa
        'default_purchase_tax_id': False,
        # Fournisseur du service: Banque centrale européenne  # noqa
        'currency_provider': 'ecb',
        # Identification *  # noqa
        'sepa_orgid_id': False,
        # Journal pour taxes sur base des paiements  # noqa
        # 'tax_cash_basis_journal_id': ctx.env.ref('__setup__.account_journal_tax_cash_basis_23').id,
        # Utiliser la comptabilité anglo-saxonne  # noqa
        'use_anglo_saxon': False,
        # Taxe de vente (%)  # noqa
        'sale_tax_rate': 0.0,
        # Utiliser dépôt de lot  # noqa
        'module_account_batch_deposit': False,
        # Interface bancaire - Synchronisez vos flux bancaires automatiquement  # noqa
        'module_account_yodlee': True,
        # Permettre les taxes sur les paiements  # noqa
        'module_account_tax_cash_basis': True,
        # Nombre de chiffres *  # noqa
        'code_digits': 7,
        # Activer la gestion des relances de paiement  # noqa
        'module_account_reports_followup': False,
        # Modèle  # noqa
        'chart_template_id': False,
        # Taxe de vente par défaut  # noqa
        'default_sale_tax_id': False,
        # Message des Paiements en retard *  # noqa
        'overdue_msg': """Dear Sir/Madam,

Our records indicate that some payments on your account are still due. Please find details below.
If the amount has already been paid, please disregard this notice. Otherwise, please forward us the total amount stated below.
If you have any queries regarding your account, Please contact us.

Thank you in advance for your cooperation.
Best Regards,""",
        # Taxe de vente par défaut  # noqa
        'sale_tax_id': False,
        # Journal des différences de taux  # noqa
        #'currency_exchange_journal_id': ctx.env.ref('__setup__.account_journal_exchange_difference_14').id,
        # Importer des fichiers .qif  # noqa
        'module_account_bank_statement_import_qif': False,
        # Compte analytique  # noqa
        'group_analytic_accounting': True,
        # Prochaine date d'exécution  # noqa
        'currency_next_execution_date': False,
        # Comptabilité analytique pour les achats  # noqa
        'group_analytic_account_for_purchases': True,
        # Date de verrouillage pour les non-conseillers  # noqa
        'period_lock_date': False,
        # Aperçu des comptes bancaires en pied de page  # noqa
        'company_footer': """False""",
        # Émetteur *  # noqa
        'sepa_orgid_issr': False,
        # Dernier mois de l'exercice: décembre  # noqa
        'fiscalyear_last_month': 12,
        # Méthode d'arrondissement des Taxes *: Arrondir à la ligne  # noqa
        'tax_calculation_rounding_method': 'round_per_line',
        # Acquéreur par défaut   # noqa
        'default_acquirer': False,
        # Taxe d'achat par défaut  # noqa
        'purchase_tax_id': False,
        # Users Receiving the Intrastat Reminder  # noqa
        'intrastat_remind_user_ids': [],
        # Compte de transfert inter-bancaire  # noqa
        #'transfer_account_id': ctx.env.ref('l10n_jp.7_transfer_account_id').id,
        
    }).execute()

@anthem.log
def account_config_settings_FR(ctx):
    """ Setup account.config.settings for RocTool SA """
    model = ctx.env['account.config.settings'].with_context({'tracking_disable':1})
    model.create({
        # Date de verrouillage  # noqa
        'fiscalyear_lock_date': False,
        # Préfixe du compte banque *  # noqa
        'bank_account_code_prefix': 512,
        # Préfixe des Comptes de Caisse *  # noqa
        'cash_account_code_prefix': 53,
        # Gestion d'actifs  # noqa
        'module_account_asset': False,
        # SEPA Pain Version *: Générique  # noqa
        'sepa_pain_version': 'pain.001.001.03',
        # Devise par défaut  # noqa
        'currency_id': ctx.env.ref('base.EUR').id,
        # Fonctions de comptabilité complète: journaux, déclarations légales, plan comptable, etc.  # noqa
        'module_account_accountant': True,
        # Dernier jour de l'exercice fiscal  # noqa
        'fiscalyear_last_day': 31,
        # Nombres de jours entre deux relances  # noqa
        'days_between_two_followups': 14,
        # Cette société a son propre plan comptable  # noqa
        'expects_chart_of_accounts': True,
        # Connecteur Plaid  # noqa
        'module_account_plaid': False,
        # Ensemble complet de taxes  # noqa
        'complete_tax_set': False,
        # ID du modèle de compte de transfert  # noqa
        'template_transfer_account_id': False,
        # Utilisez les paiements SEPA  # noqa
        'module_account_sepa': True,
        # Importer au format .csv  # noqa
        'module_account_bank_statement_import_csv': False,
        # Gestion du budget  # noqa
        'module_account_budget': False,
        # Société  # noqa
        'company_id': ctx.env.ref('base.main_company').id,
        # Comptabilité analytique pour les ventes  # noqa
        'group_analytic_account_for_sales': True,
        # Avertissement: Tous les partenaires peuvent être utilisés dans les factures  # noqa
        'group_warning_account': False,
        # Expense Journal  # noqa
        # 'expense_journal_id': ctx.env.ref('__setup__.account_journal_expense_roctool_sa').id,
        # Autoriser devises multiples  # noqa
        'group_multi_currency': True,
        # Autoriser les factures proforma  # noqa
        'group_proforma_invoices': False,
        # Reconnaissance des revenus  # noqa
        'module_account_deferred_revenue': False,
        # Obtenez des rapports comptables dynamiques  # noqa
        'module_account_reports': True,
        # La société a un plan comptable  # noqa
        'has_chart_of_accounts': False,
        # A une société par défaut  # noqa
        'has_default_company': False,
        # Compute sales tax automatically in the United States using TaxCloud.  # noqa
        'module_account_taxcloud': False,
        # Nom de votre société *  # noqa
        'sepa_initiating_party_name': "Roctool",
        # Taxe d'achat (%)  # noqa
        'purchase_tax_rate': 0.0,
        # Unité de l'intervalle: Manuellement  # noqa
        'currency_interval_unit': 'manually',
        # Importer au format .ofx  # noqa
        'module_account_bank_statement_import_ofx': True,
        # Activer l'impression et le dépôt de chèques   # noqa
        'module_l10n_us_check_printing': False,
        # Taxe d'achat par défaut  # noqa
        'default_purchase_tax_id': False,
        # Fournisseur du service: Banque centrale européenne  # noqa
        'currency_provider': 'ecb',
        # Identification *  # noqa
        'sepa_orgid_id': False,
        # Journal pour taxes sur base des paiements  # noqa
        # 'tax_cash_basis_journal_id': ctx.env.ref('__setup__.account_journal_tax_cash_basis_24').id,
        # Utiliser la comptabilité anglo-saxonne  # noqa
        'use_anglo_saxon': False,
        # Taxe de vente (%)  # noqa
        'sale_tax_rate': 0.0,
        # Utiliser dépôt de lot  # noqa
        'module_account_batch_deposit': False,
        # Interface bancaire - Synchronisez vos flux bancaires automatiquement  # noqa
        'module_account_yodlee': True,
        # Permettre les taxes sur les paiements  # noqa
        'module_account_tax_cash_basis': True,
        # Nombre de chiffres *  # noqa
        'code_digits': 6,
        # Activer la gestion des relances de paiement  # noqa
        'module_account_reports_followup': False,
        # Modèle  # noqa
        'chart_template_id': False,
        # Taxe de vente par défaut  # noqa
        'default_sale_tax_id': False,
        # Message des Paiements en retard *  # noqa
        'overdue_msg': """Madame, Monsieur,

D'après nos relevés, il semble que nous sommes encore en attente à ce jour de paiements de votre part, dont les détails sont indiqués ci-dessous.
Si ces sommes ont déjà été réglées, vous pouvez ignorer ce rappel. Dans le cas contraire, nous vous remercions de bien vouloir nous faire parvenir votre règlement.
Si vous avez d'autres questions concernant votre compte, vous pouvez nous contacter directement.

En vous remerciant par avance.

Cordialement,""",
        # Taxe de vente par défaut  # noqa
        'sale_tax_id': False,
        # Journal des différences de taux  # noqa
        #'currency_exchange_journal_id': ctx.env.ref('__setup__.account_journal_exchange_difference_15').id,
        # Importer des fichiers .qif  # noqa
        'module_account_bank_statement_import_qif': False,
        # Compte analytique  # noqa
        'group_analytic_accounting': True,
        # Prochaine date d'exécution  # noqa
        'currency_next_execution_date': False,
        # Comptabilité analytique pour les achats  # noqa
        'group_analytic_account_for_purchases': True,
        # Date de verrouillage pour les non-conseillers  # noqa
        'period_lock_date': False,
        # Aperçu des comptes bancaires en pied de page  # noqa
        'company_footer': """False""",
        # Émetteur *  # noqa
        'sepa_orgid_issr': False,
        # Dernier mois de l'exercice: décembre  # noqa
        'fiscalyear_last_month': 12,
        # Méthode d'arrondissement des Taxes *: Arrondir à la ligne  # noqa
        'tax_calculation_rounding_method': 'round_per_line',
        # Acquéreur par défaut   # noqa
        'default_acquirer': False,
        # Taxe d'achat par défaut  # noqa
        'purchase_tax_id': False,
        # Users Receiving the Intrastat Reminder  # noqa
        'intrastat_remind_user_ids': [],
        # Compte de transfert inter-bancaire  # noqa
        'transfer_account_id': ctx.env.ref('l10n_fr.1_pcg_58').id,
        
    }).execute()

@anthem.log
def account_config_settings_TW(ctx):
    """ Setup account.config.settings for RocTool Taiwan """
    model = ctx.env['account.config.settings'].with_context({'tracking_disable':1})
    model.create({
        # Date de verrouillage  # noqa
        'fiscalyear_lock_date': False,
        # Préfixe du compte banque *  # noqa
        'bank_account_code_prefix': False,
        # Préfixe des Comptes de Caisse *  # noqa
        'cash_account_code_prefix': False,
        # Gestion d'actifs  # noqa
        'module_account_asset': False,
        # SEPA Pain Version *: Générique  # noqa
        'sepa_pain_version': 'pain.001.001.03',
        # Devise par défaut  # noqa
        'currency_id': ctx.env.ref('base.TWD').id,
        # Fonctions de comptabilité complète: journaux, déclarations légales, plan comptable, etc.  # noqa
        'module_account_accountant': True,
        # Dernier jour de l'exercice fiscal  # noqa
        'fiscalyear_last_day': 31,
        # Nombres de jours entre deux relances  # noqa
        'days_between_two_followups': 14,
        # Cette société a son propre plan comptable  # noqa
        'expects_chart_of_accounts': True,
        # Connecteur Plaid  # noqa
        'module_account_plaid': False,
        # Ensemble complet de taxes  # noqa
        'complete_tax_set': False,
        # ID du modèle de compte de transfert  # noqa
        'template_transfer_account_id': False,
        # Utilisez les paiements SEPA  # noqa
        'module_account_sepa': True,
        # Importer au format .csv  # noqa
        'module_account_bank_statement_import_csv': False,
        # Gestion du budget  # noqa
        'module_account_budget': False,
        # Société  # noqa
        'company_id': ctx.env.ref('__setup__.roctool_taiwan').id,
        # Comptabilité analytique pour les ventes  # noqa
        'group_analytic_account_for_sales': True,
        # Avertissement: Tous les partenaires peuvent être utilisés dans les factures  # noqa
        'group_warning_account': False,
        # Expense Journal  # noqa
        # 'expense_journal_id': ctx.env.ref('__setup__.account_journal_expense_roctool_taiwan').id,
        # Autoriser devises multiples  # noqa
        'group_multi_currency': True,
        # Autoriser les factures proforma  # noqa
        'group_proforma_invoices': False,
        # Reconnaissance des revenus  # noqa
        'module_account_deferred_revenue': False,
        # Obtenez des rapports comptables dynamiques  # noqa
        'module_account_reports': True,
        # La société a un plan comptable  # noqa
        'has_chart_of_accounts': False,
        # A une société par défaut  # noqa
        'has_default_company': False,
        # Compute sales tax automatically in the United States using TaxCloud.  # noqa
        'module_account_taxcloud': False,
        # Nom de votre société *  # noqa
        'sepa_initiating_party_name': "RocTool SA",
        # Taxe d'achat (%)  # noqa
        'purchase_tax_rate': 0.0,
        # Unité de l'intervalle: Manuellement  # noqa
        'currency_interval_unit': 'manually',
        # Importer au format .ofx  # noqa
        'module_account_bank_statement_import_ofx': True,
        # Activer l'impression et le dépôt de chèques   # noqa
        'module_l10n_us_check_printing': False,
        # Taxe d'achat par défaut  # noqa
        'default_purchase_tax_id': False,
        # Fournisseur du service: Banque centrale européenne  # noqa
        'currency_provider': 'ecb',
        # Identification *  # noqa
        'sepa_orgid_id': False,
        # Journal pour taxes sur base des paiements  # noqa
        # 'tax_cash_basis_journal_id': ctx.env.ref('__setup__.account_journal_tax_cash_basis_25').id,
        # Utiliser la comptabilité anglo-saxonne  # noqa
        'use_anglo_saxon': False,
        # Taxe de vente (%)  # noqa
        'sale_tax_rate': 0.0,
        # Utiliser dépôt de lot  # noqa
        'module_account_batch_deposit': False,
        # Interface bancaire - Synchronisez vos flux bancaires automatiquement  # noqa
        'module_account_yodlee': True,
        # Permettre les taxes sur les paiements  # noqa
        'module_account_tax_cash_basis': True,
        # Nombre de chiffres *  # noqa
        'code_digits': 0,
        # Activer la gestion des relances de paiement  # noqa
        'module_account_reports_followup': False,
        # Modèle  # noqa
        'chart_template_id': False,
        # Taxe de vente par défaut  # noqa
        'default_sale_tax_id': False,
        # Message des Paiements en retard *  # noqa
        'overdue_msg': """Dear Sir/Madam,

Our records indicate that some payments on your account are still due. Please find details below.
If the amount has already been paid, please disregard this notice. Otherwise, please forward us the total amount stated below.
If you have any queries regarding your account, Please contact us.

Thank you in advance for your cooperation.
Best Regards,""",
        # Taxe de vente par défaut  # noqa
        'sale_tax_id': False,
        # Journal des différences de taux  # noqa
        'currency_exchange_journal_id': False,
        # Importer des fichiers .qif  # noqa
        'module_account_bank_statement_import_qif': False,
        # Compte analytique  # noqa
        'group_analytic_accounting': True,
        # Prochaine date d'exécution  # noqa
        'currency_next_execution_date': False,
        # Comptabilité analytique pour les achats  # noqa
        'group_analytic_account_for_purchases': True,
        # Date de verrouillage pour les non-conseillers  # noqa
        'period_lock_date': False,
        # Aperçu des comptes bancaires en pied de page  # noqa
        'company_footer': """False""",
        # Émetteur *  # noqa
        'sepa_orgid_issr': False,
        # Dernier mois de l'exercice: décembre  # noqa
        'fiscalyear_last_month': 12,
        # Méthode d'arrondissement des Taxes *: Arrondir à la ligne  # noqa
        'tax_calculation_rounding_method': 'round_per_line',
        # Acquéreur par défaut   # noqa
        'default_acquirer': False,
        # Taxe d'achat par défaut  # noqa
        'purchase_tax_id': False,
        # Users Receiving the Intrastat Reminder  # noqa
        'intrastat_remind_user_ids': [],
        # Compte de transfert inter-bancaire  # noqa
        'transfer_account_id': False,
        
    }).execute()


@anthem.log
def account_config_settings(ctx):
    account_config_settings_CN(ctx)
    account_config_settings_DE(ctx)
    account_config_settings_HLD(ctx)
    account_config_settings_US(ctx)
    account_config_settings_JP(ctx)
    account_config_settings_FR(ctx)
    account_config_settings_TW(ctx)
    


@anthem.log
def load_account_fiscal_position(ctx):
    """ Import account.fiscal.position from csv """
    model = ctx.env['account.fiscal.position'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.fiscal.position.csv', model)


@anthem.log
def load_account_fiscal_position_account(ctx):
    """ Import account.fiscal.position.account from csv """
    model = ctx.env['account.fiscal.position.account'].with_context({'tracking_disable':1})  # noqa
    load_csv(ctx, 'data/install/generated/account.fiscal.position.account.csv', model)


@anthem.log
def main(ctx):
    load_account_account_tag(ctx)
    load_res_currency(ctx)
    # load_account_financial_html_report_line(ctx)
    # load_account_financial_html_report(ctx)
    load_product_category(ctx)
    load_account_fiscal_position_tax(ctx)
    load_res_bank(ctx)
    add_xmlid_to_existing_ir_sequence(ctx)
    load_account_account_type(ctx)
    load_account_account(ctx)
    load_ir_sequence(ctx)
    # load_account_journal(ctx)
    # load_account_analytic_account(ctx)
    load_account_tax(ctx)
    # WE NEED THIS ! load_ir_property(ctx)
    account_config_settings(ctx)
    load_account_fiscal_position(ctx)
    load_account_fiscal_position_account(ctx)

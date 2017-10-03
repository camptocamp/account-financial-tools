# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem


@anthem.log
def create_journals(ctx):
    journal = ctx.env["account.journal"]
    companies = ctx.env["res.company"].search([])
    for company in companies:
        values = {
            "name": u"Expense {}".format(company.name),
            "type": "purchase",
            "company_id": company.id,
            "code": "EXP",
        }
        company.expense_journal_id = journal.create(values)


@anthem.log
def main(ctx):
    create_journals(ctx)

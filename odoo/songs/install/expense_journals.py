# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem
from anthem.lyrics.records import create_or_update


@anthem.log
def create_journals(ctx):
    companies = ctx.env["res.company"].search([])
    for company in companies:
        values = {
            "name": u"Expense {}".format(company.name),
            "type": "purchase",
            "company_id": company.id,
            "code": "EXP",
        }
        company.expense_journal_id = create_or_update(
            ctx, "account.journal",
            "account.expense_journal_{}".format(
                company.name.lower().replace(" ", "_").replace(".", "")
            ),
            values
        )


@anthem.log
def main(ctx):
    create_journals(ctx)

# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    journal_id = fields.Many2one(
        'account.journal',
        string='Expense Journal',
        related="company_id.expense_journal_id",
        readonly=True,
        help="The journal used when the expense is done. "
             "Configurable from Accounting settings")

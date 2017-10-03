# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class AccountConfigSettings(models.TransientModel):
    _inherit = 'account.config.settings'

    expense_journal_id = fields.Many2one(
        'account.journal',
        related='company_id.expense_journal_id',
        string="Expense Journal",
    )

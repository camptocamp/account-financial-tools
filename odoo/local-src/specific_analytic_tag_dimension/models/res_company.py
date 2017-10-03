# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    expense_journal_id = fields.Many2one(
        'account.journal',
        string='Expense Journal',
        domain="[('type', '=', 'purchase')]",
    )

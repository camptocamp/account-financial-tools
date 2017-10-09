# -*- coding: utf-8 -*-
# Author: Damien Crier
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    lead_id = fields.Many2one(comodel_name='crm.lead',
                              string="Linked Opportunity")
    survey_input_lines = fields.One2many(related='lead_id.survey_input_lines')
    contract_timeline = fields.Date(
        string="Contract timeline",
    )

    @api.onchange("date_deadline")
    def _compute_contract_timeline(self):
        # Currently any change to deadline will overwrite
        # contract timeline field as
        # there is a problem with Date fields
        # it is impossible to make "if field false" check
        # as at the moment, when you click the date field
        # it will write current date in it(if there was no default)
        # and trigger the onchange.
        for record in self:
            record.contract_timeline = record.date_deadline

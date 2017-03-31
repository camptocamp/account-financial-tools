# -*- coding: utf-8 -*-
# Author: Damien Crier
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import uuid
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo import exceptions, _
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    domain = fields.Text()
    start_date = fields.Date()
    end_date = fields.Date()
    signature_ids = fields.Many2many(comodel_name='res.partner',
                                     string="Signatures")
    project_id = fields.Many2one(
        comodel_name='project.project',
        string="Feasibility Timesheet Project",
    )
    survey_id = fields.Many2one(
        comodel_name='survey.survey',
        string="Survey",
    )
    survey_input_lines = fields.One2many(
        comodel_name='survey.user_input_line', inverse_name='lead_id',
        string='Surveys answers')
    survey_inputs = fields.One2many(
        comodel_name='survey.user_input', inverse_name='lead_id',
        string='Surveys')
    survey_input_count = fields.Integer(
        string='Survey number', compute='_count_survey_input',
        store=True)
    project_zone_id = fields.Many2one(
        comodel_name='project.zone',
        string="Project Zone",
    )
    project_process_id = fields.Many2one(
        comodel_name='project.process',
        string='Project Process',
    )
    project_market_id = fields.Many2one(
        comodel_name='project.market',
        string='Project Market'
    )
    program_manager_id = fields.Many2one(
        comodel_name='res.users',
        string='Program Manager',
        index=True,
        track_visibility='onchange',
    )

    @api.model
    def _message_get_auto_subscribe_fields(self, updated_fields,
                                           auto_follow_fields=None):
        if auto_follow_fields is None:
            auto_follow_fields = []
        auto_follow_fields = (
            set(auto_follow_fields) | {'user_id', 'program_manager_id'}
        )
        _super = super(CrmLead, self)
        return _super._message_get_auto_subscribe_fields(
            updated_fields,
            auto_follow_fields=list(auto_follow_fields),
        )

    @api.onchange('team_id')
    def onchange_team_id(self):
        if self.team_id:
            self.survey_id = self.team_id.survey_id.id
            self.project_id = self.team_id.project_id.id

    @api.depends('survey_inputs')
    def _count_survey_input(self):
        for rec in self:
            rec.survey_input_count = len(rec.survey_inputs)

    @api.multi
    def answer_selected_survey(self):
        self.ensure_one()
        survey_response_obj = self.env['survey.user_input']
        selected_survey = self.survey_id
        # if there's already a survey started (state=skip), relaunch this one
        if self.survey_inputs:
            for sur in self.survey_inputs:
                if sur.survey_id == selected_survey and sur.state != 'done':
                    url = '%s/%s' % (selected_survey.public_url, sur.token)
                    return {
                        'type': 'ir.actions.act_url',
                        'name': "Resume Survey",
                        'target': 'self',
                        'url': url,
                    }
        else:
            # else create a new one

            # generate invitation link for this partner
            # (do not send email to customer)
            token = uuid.uuid4().__str__()
            # create response with token
            now = datetime.now()
            survey_response_obj.create({
                'survey_id': selected_survey.id,
                'deadline': fields.Datetime.to_string(now + timedelta(days=1)),
                'date_create': fields.Datetime.to_string(now),
                'type': 'link',
                'state': 'new',
                'token': token,
                'lead_id': self.id,
                # 'email': self.email
                }
                )
            # get link to the survey
            url = '%s/%s' % (selected_survey.public_url, token)

            # open survey
            return {
                'type': 'ir.actions.act_url',
                'name': "Start Survey",
                'target': 'self',
                # 'target': 'new',
                'url': url,
                }

    @api.multi
    def action_result_selected_survey(self):
        self.ensure_one()
        if not self.survey_id:
            raise UserError(_('There is no selected survey to open.'))
        return self.survey_id.action_result_survey()

    def check_fields(self, fields=None):
        msg = []
        if fields:
            for f in fields:
                if not self[f]:
                    msg.append(('%s not filled.') % f)

        if msg:
            raise exceptions.Warning('\n'.join(msg))

    def check_survey_state(self):
        for s_input in self.survey_inputs:
            if s_input.state == 'done':
                return True

        raise exceptions.Warning(_('Survey not completly answered'))

    def create_linked_task(self):
        self.env['project.task'].create({'project_id': self.project_id.id,
                                         'lead_id': self.id,
                                         'name': self.name})

    @api.onchange('start_date')
    def onchange_date_start(self):
        if self.start_date:
            self.end_date = fields.Datetime.from_string(self.start_date) + \
                relativedelta(years=5)

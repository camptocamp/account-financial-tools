# -*- coding: utf-8 -*-
# Author: Damien Crier
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "RocTool specific crm module",
    "version": "10.0.1.0.0",
    "depends": ['crm',
                'survey',
                'project',
                'sales_team',
                ],
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "website": "http://www.camptocamp.com",
    "license": "GPL-3 or any later version",
    "category": "CRM",
    "data": ['security/ir.model.access.csv',
             'security/crm_security.xml',
             'data/ir_sequence.xml',
             'views/crm_lead_view.xml',
             'views/survey_templates.xml',
             'views/crm_team.xml',
             'views/project_task.xml',
             'views/partner.xml',
             'views/partner_license.xml',
             ],
    'installable': True,
}

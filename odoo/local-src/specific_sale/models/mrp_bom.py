# -*- coding: utf-8 -*-
# Author: Denis Leemann
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    project_task_id = fields.Many2one(
        'project.task',
        string='Project Task',
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        related='project_task_id.project_id',
        readonly=True,
    )

    def create_manufacture_order(self):
        self.ensure_one()
        if not all((self.picking_type_id, self.product_id)):
            raise ValidationError(
                "Please specify Product variant and Operation"
            )
        manufacture_order = self.env['mrp.production'].create({
            'bom_id': self.id,
            'product_id': self.product_id.id,
            'product_uom_id': self.product_uom_id.id,
            'picking_type_id': self.picking_type_id.id,
        })
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mrp.production',
            'target': 'current',
            'res_id': manufacture_order.id,
            'type': 'ir.actions.act_window'
        }

    def get_project_name(self):
        if not self.project_id:
            return ""
        else:
            return " [" + self.project_id.name + "]"

    @api.depends(lambda self: (self._rec_name,) if self._rec_name else ())
    def _compute_display_name(self):
        for record in self:
            record.display_name = u"{}{}".format(record.product_tmpl_id.name,
                                                 record.get_project_name())

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', (self._rec_name, operator, name),
                      ('project_id.name', operator, name)]
        pos = self.search(domain + args, limit=limit)
        return pos.name_get()

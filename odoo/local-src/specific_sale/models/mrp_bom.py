# -*- coding: utf-8 -*-
# Author: Denis Leemann
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields
from odoo.exceptions import ValidationError


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

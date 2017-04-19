# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import anthem
from anthem.lyrics.records import create_or_update


@anthem.log
def setup_admin_user(ctx):
    """ setup admin user (without portal/public) """
    groups = ctx.env['res.groups'].search([])
    groups -= ctx.env.ref('base.group_portal')
    groups -= ctx.env.ref('base.group_public')
    values = {
        'groups_id':  [(6, 0, groups.ids)],
    }
    create_or_update(ctx, 'res.users', 'base.user_root', values)


@anthem.log
def main(ctx):
    """ Main: users set up """
    setup_admin_user(ctx)

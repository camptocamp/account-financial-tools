# -*- coding: utf-8 -*-

import anthem
from anthem.lyrics.modules import uninstall


@anthem.log
def uninstall_attachment_s3(ctx):
    """ Uninstall attachment_s3 """
    uninstall(ctx, ['attachment_s3'])


@anthem.log
def pre(ctx):
    """ Pre-update """
    uninstall_attachment_s3(ctx)

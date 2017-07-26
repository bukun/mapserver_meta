# -*- coding:utf-8 -*-

import peewee

from mapmeta.core.base_model import BaseModel


class TabMapMeta(BaseModel):
    uid = peewee.CharField(null=False, index=True, unique=True,
                           primary_key=True, default='00000',
                           max_length=5, help_text='', )

    url = peewee.CharField(null=False, default='', max_length=255,
                           help_text='The path of mapfile')
    time_update = peewee.IntegerField(null=False, default=0)
    meta = peewee.TextField(null=False, default='',
                            help_text='Metadata of map')

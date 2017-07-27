# -*- coding:utf-8 -*-

'''
Model for Posts.
'''

from mapmeta.core import tools
from mapmeta.model.core_tab import TabMapMeta
from mapmeta.model.abc_model import Mabc, MHelper


class MMapMeta(Mabc):
    '''
    Model for Posts.
    '''

    def __init__(self):
        super(MMapMeta, self).__init__()

    @staticmethod
    def get_by_uid(uid):
        '''
        return the record by uid
        :param uid:
        :return:
        '''
        return MHelper.get_by_uid(TabMapMeta, uid)

    @staticmethod
    def update(uid, data_dic):
        '''
        :param uid:
        :param post_data:
        :param update_time:
        :return:
        '''

        entry = TabMapMeta.update(
            url=data_dic['url'],
            time_update=tools.timestamp(),
            meta=data_dic['meta'],
        ).where(TabMapMeta.uid == uid)
        entry.execute()

    @staticmethod
    def add_or_update( post_data):
        '''
        :param uid:
        :param post_data:
        :return:
        '''
        uid = post_data['uid']
        cur_rec = MMapMeta.get_by_uid(uid)
        if cur_rec:
            MMapMeta.update(uid, post_data)
        else:
            post_data['uid'] = uid
            MMapMeta.add_meta(post_data)

    @staticmethod
    def add_meta(data_dic):
        TabMapMeta.create(
            uid=data_dic['uid'],
            url=data_dic['url'],
            time_update=tools.timestamp(),
            meta=data_dic['meta'],
        )
        return data_dic['uid']

# -*- coding: utf-8 -*-

'''
initialize table.s
'''


from mapmeta.model.core_tab import TabMapMeta

def create_table(Tab):
    try:
        Tab.create_table()
    except:
        pass


def run_init_tables(*args):
    print('--')

    create_table(TabMapMeta)



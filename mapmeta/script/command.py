# -*- coding: utf-8 -*-

'''
Script for Command.
'''

import sys
import getopt
from .script_init import run_init


def entry(argv):
    '''
    Command entry
    :param argv:
    :return:
    '''
    command_dic = {

        'init': run_init,

    }
    try:
        # 这里的 h 就表示该选项无参数，i:表示 i 选项后需要有参数
        opts, args = getopt.getopt(argv, "hi:")
    except getopt.GetoptError:
        print('Error: helper.py -i cmd')
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print('helper.py -i cmd')
            print('cmd list ----------------------')
            print('          init: ')
            print('       migrate: ')
            print('        review: ')
            print('         -------------')
            print('      send_all: ')
            print('  send_nologin: ')
            # print('  create_admin: ')
            print('       sitemap: ')
            print('       editmap: ')
            print('    check_kind: ')
            print('         check: ')

            sys.exit()
        elif opt == "-i":

            if arg in command_dic:
                command_dic[arg](args)
                print('QED!')
            else:
                print('Wrong Command.')

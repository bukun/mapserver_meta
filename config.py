# -*- coding:utf-8 -*-

'''
Config for the website.
'''
import peewee

PORT = '8859'

DB_CON = peewee.SqliteDatabase('./database/mapmeta.db')

SITE_CFG = {
    'DEBUG': True,
    'cookie_secret': 'sadfjlk',
}

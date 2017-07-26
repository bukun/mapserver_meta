# -*- coding: utf-8 -*-

'''
script for initialization.
'''
import os
import requests
from .script_init_tabels import run_init_tables
from mapmeta.model.mapmeta_model import MMapMeta


def do_for_raster(mapserver_ip):
    '''
    代码来自 `maplet_arch//030_gen_mapproxy.py` ， 原用来找到 mapfile ， 生成 yaml .
    '''
    rst_ws = '/opt/mapws/maplet/vect3857'
    for wroot, wdirs, wfiles in os.walk(rst_ws):
        for png in wfiles:
            (lyr_name, lyr_ext) = os.path.splitext(png)
            lyr_name_arr = lyr_name.split('_')
            if png.startswith('lyr_') and len(lyr_name_arr[-1]) == 4 and lyr_name_arr[-1][0] == 'v':
                pass
            else:
                continue
            maplet_uid = lyr_name_arr[-1]
            # http://121.42.29.253/cgi-bin/mapserv?map=/opt/mapws/maplet/vect3857/China/China3857_v/mapfile.map&layer=landuse2000_v000&SERVICE=WMS&version=1.3.0&REQUEST=GetCapabilities
            mapurl = 'http://{mapserver_ip}/cgi-bin/mapserv?map={mapfile}' \
                     '&layer={layer}&SERVICE=WMS&version=1.3.0' \
                     '&REQUEST=GetCapabilities'.format(
                mapserver_ip=mapserver_ip,
                mapfile=os.path.join(wroot, 'mapfile.map'),
                layer='maplet_' + maplet_uid,
            )
            xml = requests.get(mapurl)
            print('=' * 20)
            print(maplet_uid)
            print(mapurl)
            print(xml.text)
            mapinfo = {
                'uid': maplet_uid,
                'url': mapurl,
                'meta': xml.text
            }
            MMapMeta.add_meta(mapinfo)


def run_init(*args):
    '''
    running init.
    :return:
    '''
    run_init_tables()
    do_for_raster('121.42.29.253')

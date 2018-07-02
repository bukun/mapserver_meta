# -*- coding: utf-8 -*-

'''
script for initialization.
'''
import os
import requests
from .script_init_tabels import run_init_tables
from mapmeta.model.mapmeta_model import MMapMeta
from lxml import etree

def do_for_maplet(mapserver_ip):
    '''
    代码来自 `maplet_arch//030_gen_mapproxy.py` ， 原用来找到 mapfile ， 生成 yaml .
    '''
    rst_ws = '/opt/mapws/maplet/00_China_png'
    for wroot, wdirs, wfiles in os.walk(rst_ws):
        for png in wfiles:
            (lyr_name, lyr_ext) = os.path.splitext(png)
            if png.endswith('.png') :
                pass
            else:
                continue
            maplet_uid = lyr_name
            # http://121.42.29.253/cgi-bin/mapserv?map=/opt/mapws/maplet/vect3857/China/China3857_v/mapfile.map&layer=landuse2000_v000&SERVICE=WMS&version=1.3.0&REQUEST=GetCapabilities
            mapurl = 'http://{mapserver_ip}/cgi-bin/mapserv?map=/opt/mapws/maplet/maplet_00.map' \
                     '&layer={layer}&SERVICE=WMS&version=1.3.0' \
                     '&REQUEST=GetCapabilities'.format(
                mapserver_ip=mapserver_ip,
                layer='maplet_' + maplet_uid,
            )
            print(mapurl)
            # xml = requests.get(mapurl)
            lyr_meta = get_meta(mapurl, maplet_uid)
            mapinfo = {
                'uid': maplet_uid,
                'url': mapurl,
                'meta': lyr_meta
            }
            MMapMeta.add_or_update(mapinfo)
def get_meta(url, sig):
    uu = requests.get(url)
    uu.encoding='utf-8'

    uu.encoding

    xml_text = uu.text

    xml_text2 = xml_text.encode('utf-8')
    root = etree.XML(xml_text2) # xml_text 为xml纯文本文件

    root.tag



    namespace = "{http://www.opengis.net/wms}"

    uu = root.findall('.//{0}Layer'.format(namespace))
    bb = ''
    for x in uu:
    #     print(x.tag)
    #     print(x.attrib)

        tt = x.find('.//{0}Name'.format(namespace))

        # tt = x.getroottree()
        sig_arr = tt.text.split('_')

        if sig_arr[-1] == sig:
            bb= etree.tostring(x,  pretty_print=True).decode()
    return bb


def do_for_vector(mapserver_ip):
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
            print(mapurl)


            # print(the_html)
            #for uu in the_html.iter():
            #    print(uu.tag)


            lyr_meta = get_meta(mapurl, maplet_uid)
            mapinfo = {
                'uid': maplet_uid,
                'url': mapurl,
                'meta': lyr_meta
            }
            MMapMeta.add_or_update(mapinfo)


def run_init(*args):
    '''
    running init.
    :return:
    '''
    run_init_tables()
    do_for_vector('121.42.29.253')
    do_for_maplet('121.42.29.253')


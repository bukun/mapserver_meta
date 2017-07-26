# -*- coding:utf-8 -*-

'''
The basic HTML Page handler.
'''

from concurrent.futures import ThreadPoolExecutor
from mapmeta.core.base_handler import BaseHandler
from mapmeta.model.mapmeta_model import MMapMeta


class PostHandler(BaseHandler):
    '''
    The basic HTML Page handler.
    '''
    executor = ThreadPoolExecutor(2)

    def initialize(self, **kwargs):
        super(PostHandler, self).initialize()

        if 'kind' in kwargs:
            self.kind = kwargs['kind']
        else:
            self.kind = '1'

        self.filter_view = kwargs['filter_view'] if 'filter_view' in kwargs else False

    def get(self, *args, **kwargs):
        url_arr = self.parse_url(args[0])

        if len(url_arr) == 1:
            self._gen_uid(url_arr[0])


        else:
            kwd = {
                'title': '',
                'info': '404. Page not found!',
            }
            self.set_status(404)
            self.render('misc/html/404.html', kwd=kwd)

    def index(self):
        '''
        The default page of POST.
        '''
        self.render('post_{0}/post_index.html'.format(self.kind),
                    kwd={'uid': '', })

    def _gen_uid(self, uid):
        '''
        Generate the ID for post.
        :return: the new ID.
        '''
        self.set_header('Content-Type', 'text/xml')
        info = MMapMeta.get_by_uid(uid)

        self.write(info.meta)
        # self.render('meta/mapmeta.html', mapmeta=info.meta)

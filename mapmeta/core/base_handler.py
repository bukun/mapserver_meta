# -*- coding:utf-8 -*-

'''
Basic for handler
'''

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    '''
    The base class for handlers.
    '''

    def initialize(self, **kwargs):
        super(BaseHandler, self).initialize()

    def get_post_data(self):
        '''
        Get all the arguments from post request. Only get the first argument by default.
        :return: post_data.
        '''
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_arguments(key)[0]
        return post_data

    # pylint: disable=R0201
    def parse_url(self, url_str):
        '''
        split the url_str to array.
        :param url_str: the request url.
        :return: the array of request url.
        '''
        url_str = url_str.strip()
        return url_str.split('/') if url_str else []

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def data_received(self, chunk):
        return False

# -*- coding:utf-8 -*-



from mapmeta.handlers.post_handler import PostHandler

urls = [

    ("/meta/(.*)", PostHandler, dict()),

]

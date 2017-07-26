# -*- coding:utf-8 -*-

'''
The router used in App.
'''

import router
import mapmeta.core.router

urls = router.urls + mapmeta.core.router.urls

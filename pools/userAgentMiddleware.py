# -*- coding: utf-8 -*-
from utils import utils


class userAgentMiddleware(object):
    # 动态随机设置 User-agent
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', utils.getUserAgent())
        request.headers.setdefault('Referer', request.url)

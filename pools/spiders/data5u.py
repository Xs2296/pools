# -*- coding: utf-8 -*-
import scrapy
import re
from pools.items import PoolsItem


class data5uSpider(scrapy.Spider):
    name = 'data5u'
    allowed_domains = ['data5u.com']
    start_urls = ['http://www.data5u.com/free/gngn/index.shtml']

    def parse(self, response):
        node_list = response.xpath("//ul[@class='l2']")
        for node in node_list:
            item = PoolsItem()
            item['host'] = node.xpath('./span[1]/li/text()').extract_first()
            item['port'] = node.xpath('./span[2]/li/text()').extract_first()
            item['http'] = node.xpath('./span[4]/li/text()').extract_first().lower()
            item['anonymity'] = node.xpath('./span[3]/li/text()').extract_first()
            speed = node.xpath('./span[8]/li/text()').extract_first()
            item['speed'] = re.sub(r'[^\x00-\x7F]+', '', speed).strip()
            item['address'] = node.xpath('./span[6]/li/text()').extract_first()
            item['sources'] = 'data5u'
            yield item

# -*- coding: utf-8 -*-
import scrapy
import re
from pools.items import PoolsItem


class xiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/']

    def parse(self, response):
        node_list = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        for node in node_list:
            item = PoolsItem()
            item['host'] = node.xpath('./td[2]/text()').extract_first()
            item['port'] = node.xpath('./td[3]/text()').extract_first()
            item['http'] = node.xpath('./td[6]/text()').extract_first().lower()
            item['anonymity'] = node.xpath('./td[5]/text()').extract_first()
            speed = node.xpath("./td[@class='country'][3]/div[@class='bar']/@title").extract_first()
            item['speed'] = re.sub(r'[^\x00-\x7F]+', '', speed).strip()
            item['address'] = node.xpath('./td[4]/a/text()').extract_first()
            item['sources'] = 'xicidaili'
            yield item

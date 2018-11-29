# -*- coding: utf-8 -*-
import scrapy
import re
from pools.items import PoolsItem


class kuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free']

    def parse(self, response):
        node_list = response.xpath("//table[@class='table table-bordered table-striped']/tbody/tr")
        for node in node_list:
            item = PoolsItem()
            item['host'] = node.xpath('./td[1]/text()').extract_first()
            item['port'] = node.xpath('./td[2]/text()').extract_first()
            item['http'] = node.xpath('./td[4]/text()').extract_first().lower()
            item['anonymity'] = node.xpath('./td[3]/text()').extract_first()
            speed = node.xpath('./td[6]/text()').extract_first()
            item['speed'] = re.sub(r'[^\x00-\x7F]+', '', speed).strip()
            item['address'] = node.xpath('./td[5]/text()').extract_first()
            item['sources'] = 'kuaidaili'
            yield item

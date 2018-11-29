# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
from .items import Pools


class PoolsPipeline(object):
    def process_item(self, item, spider):
        item = dict(item)
        if Pools.table_exists() == False:
            Pools.create_table()
        try:
            query = Pools.select().where(Pools.host == item['host'], Pools.port == item['port'],Pools.sources == item['sources'])
            if query.count() == 0:
                Pools.create(
                    host=item['host'],
                    port=item['port'],
                    http=item['http'],
                    anonymity=item['anonymity'],
                    speed=item['speed'],
                    address=item['address'],
                    sources=item['sources'],
                    create_time=datetime.datetime.now()
                )
        except Exception as e:
            pass
        return item

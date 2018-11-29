# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from peewee import *
import config

db = MySQLDatabase(config.DB_NAME, host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, passwd=config.DB_PWD,charset='utf8')


class PoolsItem(scrapy.Item):
    host = scrapy.Field()
    port = scrapy.Field()
    http = scrapy.Field()
    anonymity = scrapy.Field()
    speed = scrapy.Field()
    address = scrapy.Field()
    sources = scrapy.Field()


class Pools(Model):
    host = CharField(max_length=100)
    port = CharField(max_length=10)
    http = CharField(max_length=10)
    anonymity = CharField(max_length=100)
    speed = CharField(max_length=10)
    address = CharField(max_length=255, null=True)
    sources = CharField(max_length=100)
    status = FloatField(default=0)
    check_time = DateTimeField(null=True)
    create_time = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = config.TABLE_NAME

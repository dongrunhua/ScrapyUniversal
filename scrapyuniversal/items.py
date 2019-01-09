# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class NewsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()
    content = Field()
    datetime = Field()
    source = Field()
    website = Field()
    crawled_at = Field()

class WallStreetNewsItem(Item):
    digest = Field()
    title = Field()
    url = Field()
    content = Field()
    datetime = Field()
    source = Field()
    website = Field()
    crawled_at = Field()
    image = Field()

class FinanceItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()
    content = Field()
    datetime = Field()
    source = Field()
    website = Field()
    crawled_at = Field()

class ChinaCourt(Item):

    title = Field()
    content = Field()
    url = Field()
    message = Field()
    website = Field()
    crawled_at = Field()
    datetime = Field()
    source = Field()

class ChinaMessage(Item):

    title = Field()
    content = Field()
    url = Field()
    website = Field()
    crawled_at = Field()

class HuaLv(Item):

    title = Field()
    content = Field()
    website = Field()
    source = Field()
    crawled_at = Field()
    url = Field()
    datetime = Field()

class QiDian(Item):
    name = Field()
    number_words = Field()
    title = Field()
    content = Field()
    main =  Field()
    crawled_at = Field()


class XueQiu(Item):
    title = Field()
    content = Field()
    url = Field()


class Sina_Finance(Item):
    title = Field()
    content = Field()


class Rong360(Item):
    title = Field()
    content = Field()


class Zhiku(Item):
    ID = Field()
    PID = Field()
    name = Field()


class ZhikuContent(Item):
    category_id = Field()
    name = Field()
    description = Field()
    related_words = Field()

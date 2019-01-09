# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



import pymongo
import time


class TimePipeline(object):

    def process_item(self, item, spider):
        # if isinstance(item, UserItem) or isinstance(item, WeiboItem):
        now = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        item['crawled_at'] = now
        return item

class HandleDate(object):

    def process_item(self,item,spider):

        # item = dict(item)
        item['main'] = [{
            "content":item['content'],
            "number_words":item['number_words'],
            "chapter":item['title'],
            "crawled_at":item['crawled_at']
        }]

        del item['content']
        del item['number_words']
        del item['title']
        del item['crawled_at']
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db,mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'),mongo_collection=crawler.settings.get('MONGO_COLLECTION'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        # 去重操作


        #if list(self.db[self.mongo_collection].find({"name": item['name']})):
            #self.db[self.mongo_collection].update(
                #{"name": item["name"]},
                #{"$addToSet": {"main": {"$each": item['main']}}})
            #return item
        #else:
        self.db[self.mongo_collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import *
from scrapyuniversal.loaders import *
from scrapyuniversal.utils import get_config
from scrapyuniversal import urls
from scrapyuniversal.rules import rules
from scrapyuniversal.process_links import *
from scrapyuniversal.parse import *
from lxml import etree
import re


class UniversalSpider(CrawlSpider):
    name = 'universal'


    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.spider_name = name
        self.config = config
        self.num = 1
        self.rules = rules.get(config.get('rules'))
        start_urls = config.get('start_urls')
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':
                self.start_urls = list(eval('urls.' + start_urls.get('method'))(*start_urls.get('args', [])))
        self.allowed_domains = config.get('allowed_domains')
        super(UniversalSpider, self).__init__(*args, **kwargs)


    def parse_item(self, response,PID=None):

        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls, response=response)
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, eval(*extractor.get('args')))
            yield loader.load_item()


    def process_links(self, links):
        '''处理http和https之间的转换'''
        if self.config.get('process_links'):
            result = eval(self.spider_name)(links)
            return result
        return links


    def parse(self, response):
        '''主要处理ajax请求的返回的response'''
        if self.config.get('parse'):
            result = eval(self.spider_name)(response.text,self)
            return result
        return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)
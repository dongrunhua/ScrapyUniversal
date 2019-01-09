from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


rules = {

    'rong360':(Rule(LinkExtractor(allow='.*',restrict_xpaths='//a[contains(., "下一页")]'))
               ,Rule(LinkExtractor(allow='.*',restrict_css='.act-list li h3 a'),callback='parse_item')),

}






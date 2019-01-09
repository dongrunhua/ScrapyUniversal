import json
from pprint import pprint
from scrapy import Request


def wall_street(param,spider):
    url_list = []
    dict_param = json.loads(param)

    if dict_param['data']['next_cursor']:
        base_url = 'https://api-prod.wallstreetcn.com/apiv1/content/articles?category=global&limit=100&cursor='
        next_url =base_url+dict_param['data']['next_cursor']
        url_list.insert(0,Request(next_url))

    for item in dict_param['data']['items']:
        if item.get('uri').startswith('https://wallstreetcn.com/articles/'):
            url = item.get('uri')
            url_list.append(Request(url, spider.parse_item))

    return url_list



def xueqiu(param,spider):
    url_list = []
    dict_param = json.loads(param)
    if dict_param['next_max_id']:
        base_url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id={}&count=20&category=-1'
        next_url = base_url.format(dict_param['next_max_id'])
        url_list.insert(0,Request(next_url))

    for item in dict_param['list']:
        base_url = 'https://xueqiu.com'
        if not json.loads(item['data']).get('target').startswith('/S'):
            code = json.loads(item['data']).get('target')
            url_list.append(Request(base_url+code,spider.parse_item))

    return url_list


def sina_finance(param,spider):
    dict_param = json.loads((param))

    for data in dict_param['result']['data']:
        yield Request(data['url'],spider.parse_item)


def trip(param,spider):
    dict_param = json.loads(param)

    for data in dict_param['data']['docs']:
        yield Request(data['url'],spider.parse_item)
'''负责把生成url'''
from time import time

def china(start, end):
    for page in range(start, end + 1):
        yield 'https://tech.china.com/articles/index_' + str(page) + '.html'


def wall_street():
    yield 'https://api-prod.wallstreetcn.com/apiv1/content/articles?category=global&limit=100&cursor='+str(int(time()))+','+str(int(time()))


def chinamessage():
    base_url = 'http://law.npc.gov.cn/FLFG/flfgByID.action?flfgID={}'
    with open('./code.txt','r') as f:
        codes = f.read().split("|")
        for code in codes:
            yield base_url.format(code)

def xueqiu():
    yield 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=-1'


def sina_finance():
    for page in range(1,23001):
        yield 'http://feed.mix.sina.com.cn/api/roll/get?pageid=155&lid=1686&num=50&page='+str(page)


def trip():
    base_url = 'http://interface.sina.cn/travel/2017/index_newslist.d.json?type=hot'
    for page in range(1,159):
        url = base_url+'&page='+str(page)
        for cardpage in range(1,4):
            yield url+'&cardpage='+str(cardpage)


def wikipedia():
    base_url = 'https://zh.wikipedia.org/wiki/Wikipedia:新条目推荐/{y}年{m}月'

    for year in range(2005,2019):
        for month in range(1,13):

            if year == 2015 and month < 3:
                continue
            if year == 2018 and month > 10:
                break

            yield base_url.format(y=str(year),m=str(month))
'''负责过滤提取出来的请求'''
import pymongo
MONGO_URL = 'localhost'
MONGO_DB = 'law'
MONGO_COLLECTION = 'hualv'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def china(links):
    '''处理http和https之间的转换'''
    for index, link in enumerate(links):
        link.url = link.url.replace('http', 'https')
        links[index] = link
    return links


def hualv(links):

    urls = links[:]
    for index,link in enumerate(links):
        url = link.url
        if list(db.hualv.find({"url":url})) :
            urls.remove(link)
            print("<"+url+">","无需爬取")
    return urls

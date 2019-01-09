from os.path import realpath, dirname
import json


def get_config(name):
    '''
    负责加载json数据
    :param name: 爬虫的名字
    :return: json数据
    '''
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
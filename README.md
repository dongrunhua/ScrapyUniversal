# ScrapyUniversal

## 安装

### 安装Python

至少Python3.5以上

### ChromeXpath插件

将ChromeXpath/XPath-Helper_v2.0.2.crx 安装到chrome浏览器中

安装成功如下图

![Image text](https://github.com/dongrunhua/ScrapyUniversal/raw/master/img-folder/%E5%AE%89%E8%A3%85xpath%20%E5%9B%BE.png)

### MongoDB

安装好之后将MongoDB服务开启

#### 安装依赖

```
pip3 install -r requirements.txt
```
## 文件说明

- configs/*

> 配置文件（一个爬虫一个json）

- item.py

> 定义爬取字段

- loaders.py

> 清洗数据功能

- middlewares.py

> 自定义中间键（一般用于ProxyPool、CookiePool）

- parse.py

> ajax请求 返回json数据格式时需开启功能

- pipelines.py

> 一般用于过滤、处理、保存爬取下来的数据

- process_links.py

> 处理跟进链接

- rules.py

> 跟进链接逻辑的定义

- setting.py

> scrapy默认配置文件

- urls.py

> 动态生成 starturl 

- utils.py

> 读取 json 配置文件工具

- CreateConfig.py

> GUI界面创建 conifgs/*.json 文件

- run.py

> 启动函数

#### 启动函数

```
python run.py SpiderName
```
#### demo1

目标网站
https://www.rong360.com/gl/daikuangonglue/gongluepindao/

爬取6691页的每一条新闻

![Image text](https://github.com/dongrunhua/ScrapyUniversal/raw/master/img-folder/demo1%E5%9B%BE%E7%89%871.png)

##### 第一步

- 运行 CreateConfig.py

或者

- 直接在configs/下创建json配置文件

这里以运行CreateConfig.py为例

- 运行CreateConfig.py后会出现如下窗口

![Image text](https://github.com/dongrunhua/ScrapyUniversal/raw/master/img-folder/demo1%20%E5%9B%BE%E7%89%872.png)

##### 第二步

###### 依次填写窗口文本框内容

- SpiderName : rong360  # 目标网址简称

- TargetWebsiteIndex : www.rong360.com/  # 目标网站主页 *最后需要带/

- BrowserVersion : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36  # 浏览器版本

- DataSaveChoice : 点击MongoDB ==> MongoUri : localhost  MongoDB : news   MongoCollection : rong360 点击Commit  # MongoDB和MongoCollection无需实现创建

- AllowedDomains : rong360.com  

- StartUrl : static  并且点击AddValue ==> StartUrlValue : https://www.rong360.com/gl/daikuangonglue/gongluepindao/ 点击Commit # 这里的StartUrl 是静态的无需动态生成 所以是static
    
- FollowUrlRules : rong360  # 必须要与SpiderName值相同  同时需要在rules.py定义逻辑


```python
rules = {
    
    'rong360':(Rule(LinkExtractor(allow='.*',restrict_xpaths='//a[contains(., "下一页")]'))   # 递归点击下一页  .*是正则表达式  //a[contains(., "下一页")]是xpath语法 表示含有下一页text的a标签
               ,Rule(LinkExtractor(allow='.*',restrict_css='.act-list li h3 a'),callback='parse_item')),  # 点击每一页news的详情页  '.act-list li h3 a' css语法 parse_item是回调函数 解析详情页         
}
```
Rules 使用文档 https://doc.scrapy.org/en/latest/topics/link-extractors.html?highlight=Rules

xpath css 使用文档 https://doc.scrapy.org/en/latest/topics/selectors.html

- FollowUrlChange : false  # 本 demo 无需处理跟进链接 既是 false

- AjaxRequest : false  # 本 demo 不是 ajax 请求 既是 false

- Field : Rong360  # 需要在 item.py下定义Item的子类  我这里只定义2个字段 title content  

```python
class Rong360(Item):
    title = Field()
    content = Field()
```
字段既是存储在 mongo 中的 key

- Loader : DefaultLoader # 一般是 DefaultLoader

- Attribute : 点击AddAttr ==>  Name : title # 必须要与 item定义子类的属性一一对应 Method : xpath  # 这里使用xpath选择器也可以使用css  args ：/html/body/div[3]/div[2]/div[1]/div[1]/h1/text()  Re :  # 本demo无需使用正则 点击提交
                            Name : content # 必须要与 item定义子类的属性一一对应 Method : css  # 这里使用css选择器也可以使用xpath  args ：.act-content p::text  Re :  # 本demo无需使用正则 点击提交
                            
- - ChromeXpath使用法

![Image text](https://github.com/dongrunhua/ScrapyUniversal/raw/master/img-folder/xpath%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95.png)

- CommitButton : 点击Commit 

- - 第二步最终效果图

![Image text](https://github.com/dongrunhua/ScrapyUniversal/raw/master/img-folder/%E7%AC%AC%E4%BA%8C%E6%AD%A5%E6%9C%80%E7%BB%88%E6%95%88%E6%9E%9C%E5%9B%BE.png)

##### 第三步

- 命令行运行 scrapy

```
python run.py rong360
```

- 运行成功效果图

![Image text](https://github.com/dongrunhua/ScrapyUniversal/raw/master/img-folder/demo1%E6%88%90%E5%8A%9F%E5%9B%BE%E7%89%87.png)

![Image text](https://github.com/dongrunhua/ScrapyUniversal/raw/master/img-folder/demo1%E6%88%90%E5%8A%9F%E7%88%AC%E5%8F%96%E5%86%85%E5%AE%B9%E5%9B%BE.png)

- Mongodb 数据存储图

![Image text](https://github.com/dongrunhua/ScrapyUniversal/raw/master/img-folder/mongodb%20%E6%95%B0%E6%8D%AE%E5%AD%98%E5%82%A8%E5%9B%BE.png)

- Mongodb图形界面客户端推荐使用 Robo 3T

- 后期会吧ProxyPool CookiePool 增加进去
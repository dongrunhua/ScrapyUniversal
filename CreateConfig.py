import tkinter as tk
from tkinter import ttk
from tkinter import *
from pprint import pprint
import json

with open('scrapyuniversal/configs/template.json', 'r') as f:
    template_json = json.loads(f.read())

def GetMongoConfig(MONGOURIWin,MONGODBWin,MONGOCOLLECTIONWin):
    MONGO_URI = MONGOURIWin.get()
    MONGO_DB = MONGODBWin.get()
    MONGO_COLLECTION = MONGOCOLLECTIONWin.get()

    template_json['settings']['MONGO_URI'] = MONGO_URI
    template_json['settings']['MONGO_DB'] = MONGO_DB
    template_json['settings']['MONGO_COLLECTION'] = MONGO_COLLECTION

    MONGOURIWin.delete(0, END)
    MONGODBWin.delete(0, END)
    MONGOCOLLECTIONWin.delete(0, END)

def MongoDBConfig():

    dbwin = tk.Tk()
    dbwin.title('MongoDB配置')

    MONGOURI = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(dbwin, text="MongoUri")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=0)
    MONGOURIWin = ttk.Entry(dbwin, width=30,textvariable=MONGOURI)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    MONGOURIWin.grid(column=2, row=0)

    MONGODB = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(dbwin, text="MongoDB")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=1)
    MONGODBWin = ttk.Entry(dbwin, width=30,textvariable=MONGODB)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    MONGODBWin.grid(column=2, row=1)

    MONGOCOLLECTION = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(dbwin, text="MongoCollection")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=2)
    MONGOCOLLECTIONWin = ttk.Entry(dbwin, width=30,textvariable=MONGOCOLLECTION)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    MONGOCOLLECTIONWin.grid(column=2, row=2)

    Commit = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(dbwin, text="Commit")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=3)
    AddAttr = ttk.Button(dbwin, width=30, text='Commit', command=lambda : GetMongoConfig(MONGOURIWin=MONGOURIWin, MONGODBWin=MONGODBWin, MONGOCOLLECTIONWin=MONGOCOLLECTIONWin) )
    AddAttr.grid(column=2, row=3)

    dbwin.mainloop()

def GetStartUrlValue(StartUrlValueWin):
    value = StartUrlValueWin.get()
    template_json['start_urls']['value'].append(value)
    StartUrlValueWin.delete(0,END)

def StartUrlValue():

    StartUrlwin = tk.Tk()
    StartUrlwin.title('增加StartUrl')
    StartUrl = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(StartUrlwin, text="StartUrlValue")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=0)
    StartUrlValueWin = ttk.Entry(StartUrlwin, width=50,textvariable=StartUrl)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    StartUrlValueWin.grid(column=2, row=0)

    Commit = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(StartUrlwin, text="Commit")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=1)
    AddAttr = ttk.Button(StartUrlwin, width=45, text='Commit',command=lambda: GetStartUrlValue(StartUrlValueWin=StartUrlValueWin))
    AddAttr.grid(column=2, row=1)
    StartUrlwin.mainloop()



def  GetAttrValue(NameWin,MethodWin,ArgsWin,ReWin):
    NameWin = NameWin.get()
    MethodWin = MethodWin.get()
    ArgsWin = ArgsWin.get()
    ReWin = ReWin.get()

    template_json['item']['attrs'][NameWin] = [{'method':MethodWin,'args':[ArgsWin]}]
    if ReWin:
        template_json['item']['attrs'][NameWin][0]['re'] = ReWin

    NameWin.delete(0, END)
    MethodWin.delete(0, END)
    ArgsWin.delete(0, END)
    ReWin.delete(0, END)


def AttrValue():

    Attrwin = tk.Tk()
    Attrwin.title('字段提取属性')

    Name = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(Attrwin, text="Name")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=0)
    NameWin = ttk.Entry(Attrwin, width=60,textvariable=Name)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    NameWin.grid(column=2, row=0)

    Method = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(Attrwin, text="Method")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=1)
    MethodWin = ttk.Entry(Attrwin, width=60,textvariable=Method)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    MethodWin.grid(column=2, row=1)

    Args = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(Attrwin, text="Args")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=2)
    ArgsWin = ttk.Entry(Attrwin, width=60,textvariable=Args)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    ArgsWin.grid(column=2, row=2)

    Re = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(Attrwin, text="Re")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=3)
    ReWin = ttk.Entry(Attrwin, width=60,textvariable=Re)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    ReWin.grid(column=2, row=3)

    Commit = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(Attrwin, text="Commit")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=4)
    AddAttr = ttk.Button(Attrwin, width=60, text='Commit',command=lambda: GetAttrValue(NameWin=NameWin,MethodWin=MethodWin,ArgsWin=ArgsWin,ReWin=ReWin))
    AddAttr.grid(column=2, row=4)
    Attrwin.mainloop()

def GetTextValue():

    SpiderName = SpiderWin.get()
    index = WebIndexWin.get()
    USER_AGENT = BrowserVersionWin.get()
    process_links = ProcessLinksWin.get()
    parse = AjaxWin.get()
    start_urls = StartUrlWin.get()
    allowed_domains = AllowedDomainsWin.get()
    rules = RulesWin.get()
    item = ItemsWin.get()
    loader = DefaultLoaderWin.get()

    template_json['index'] = index
    template_json['settings']['USER_AGENT'] = USER_AGENT
    template_json['process_links'] = False if process_links == 'false' else True
    template_json['parse'] = False if parse == 'false' else True
    template_json['start_urls']['type'] = start_urls
    template_json['allowed_domains'] = [allowed_domains]
    template_json['rules'] = rules
    template_json['item']['class'] = item
    template_json['item']['loader'] = loader

    pprint(template_json)
    with open('scrapyuniversal/configs/%s.json'%SpiderName,'w') as f:
        json.dump(template_json, f, ensure_ascii=False)



if __name__ == '__main__':
    '''
      创建gui窗口
    '''
    win = tk.Tk()

    win.title("UniversalSpider")


    SpiderNmae = tk.StringVar()  # 创建Spider 框框
    aLabel = ttk.Label(win, text="SpiderName")  # 创建标签, text：显示输入的内容
    aLabel.grid(column=1, row=0)
    SpiderWin = ttk.Entry(win, width=100,textvariable=SpiderNmae)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    SpiderWin.grid(column=2, row=0)
    SpiderNmae.set('e.g:zhihu')


    WebIndex = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(win, text="TargetWebsiteIndex")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=1)
    WebIndexWin = ttk.Entry(win, width=100,textvariable=WebIndex)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    WebIndexWin.grid(column=2, row=1)
    WebIndex.set('e.g:https://www.zhihu.com/')


    BrowserVersion = tk.StringVar()  # 创建浏览器版本号 框框
    aLabel = ttk.Label(win, text="BrowserVersion")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=2)
    BrowserVersionWin = ttk.Entry(win, text='',width=100,textvariable=BrowserVersion)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    BrowserVersionWin.grid(column=2, row=2)
    BrowserVersion.set('e.g:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')


    aLabel = ttk.Label(win, text="DataSaveChoice")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=3,)
    mongodb = ttk.Button(win, text='MongoDB', command=MongoDBConfig)
    mongodb.grid(column=2,row=3,sticky=W)
    mysql = ttk.Button(win, text='Json', command=GetTextValue)
    mysql.grid(column=2, row=3)
    excel = ttk.Button(win, text='Excel', command=GetTextValue)
    excel.grid(column=2, row=3,sticky=E)


    ProcessLinks = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(win, text="FollowUrlChange")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=7)
    ProcessLinksWin = ttk.Entry(win, width=100,textvariable=ProcessLinks)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    ProcessLinksWin.grid(column=2, row=7)
    ProcessLinks.set('default:false')


    Ajax = tk.StringVar()  # 创建目标网站 index 框框
    aLabel = ttk.Label(win, text="AjaxRequest ")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=8)
    AjaxWin = ttk.Entry(win, width=90,textvariable=Ajax)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    AjaxWin.grid(column=2, row=8,sticky=W)
    Ajax.set('default:false    (一般启用是 ajax 请求) True 需在/Users/ahua/Desktop/ScrapyUniversal/scrapyuniversal/parse.py增加逻辑')


    StartUrl = tk.StringVar()
    aLabel = ttk.Label(win, text="StartUrl")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=5)
    StartUrlWin = ttk.Entry(win, width=90, textvariable=StartUrl)  # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    StartUrlWin.grid(column=2, row=5,sticky=W)
    StartUrl.set('default:static')
    StartUrlDynamic = ttk.Button(win, text='AddValue', command=StartUrlValue)
    StartUrlDynamic.grid(column=2, row=5, sticky=E)


    AllowedDomains = tk.StringVar()
    aLabel = ttk.Label(win, text="AllowedDomains")  # 创建一个标签, text：显示翻译结果的内容
    aLabel.grid(column=1, row=4)
    AllowedDomainsWin = ttk.Entry(win, width=100, textvariable=AllowedDomains)
    AllowedDomainsWin.grid(column=2, row=4)
    AllowedDomains.set('e.g:zhihu.com')


    Rules = tk.StringVar()
    aLabel = ttk.Label(win, text="FollowUrlRules")
    aLabel.grid(column=1, row=6)
    RulesWin = ttk.Entry(win, width=100, textvariable=Rules)
    RulesWin.grid(column=2, row=6)
    Rules.set('e.g:zhihu      同时增加：/ScrapyUniversal/scrapyuniversal/rules.py文件下的rules字典定义规则必须和SpiderName相同')

    Items = tk.StringVar()
    aLabel = ttk.Label(win, text="Field")
    aLabel.grid(column=1, row=9)
    ItemsWin = ttk.Entry(win, width=100, textvariable=Items)
    ItemsWin.grid(column=2, row=9)
    Items.set('e.g:Zhihu      同时增加：/ScrapyUniversal/scrapyuniversal/items.py文件Item的子类')

    DefaultLoader = tk.StringVar()
    aLabel = ttk.Label(win, text="Loader")
    aLabel.grid(column=1, row=10)
    DefaultLoaderWin = ttk.Entry(win, width=100, textvariable=DefaultLoader)
    DefaultLoaderWin.grid(column=2, row=10)
    DefaultLoader.set('default:DefaultLoader')

    Attribute = tk.StringVar()
    aLabel = ttk.Label(win, text="Attribute")
    aLabel.grid(column=1, row=11)
    AttributerWin = ttk.Entry(win, width=100, textvariable=Attribute)
    AttributerWin.grid(column=2, row=11)
    Attribute.set('Extraction rules for fields 与Field对应')
    AddAttr = ttk.Button(win, text='AddAttr', command=AttrValue)
    AddAttr.grid(column=2, row=11, sticky=E)

    Commit = tk.StringVar()
    aLabel = ttk.Label(win, text="CommitButton")
    aLabel.grid(column=1, row=12)
    AddAttr = ttk.Button(win, width=60,text='Commit', command=GetTextValue)
    AddAttr.grid(column=2, row=12)


    # AddAttr = ttk.Button(win,  width=100,text='AddAttr', command=GetTextValue)
    # AddAttr.grid(column=2, row=1)
    # inputWin.bind('<FocusIn>', focusIn)
    # inputWin.bind('<Key-Return>', event)  # 绑定回车事件 返回执行结果
    # inputWin.focus()  # 初始化文本框获取焦点
    win.wm_attributes('-topmost', 1)  # 让窗口置顶
    win.mainloop()  # 显示窗口

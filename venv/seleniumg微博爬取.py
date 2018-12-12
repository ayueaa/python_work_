from selenium import webdriver
from urllib.parse import quote
from pyquery import PyQuery as pq
import time
import pymongo

broswer=webdriver.Chrome()
id_name="十七十八一枝花"
url="https://m.weibo.cn/u/2202955263?uid=2202955263&luicode=10000011&lfid=100103type=1&q="+quote(id_name)
broswer.get(url)
time.sleep(3)
for i in range(60):
    broswer.execute_script("window.scrollTo(0,200000000)")
    time.sleep(1)
time.sleep(2)
html=broswer.page_source
doc=pq(html)
shadow=doc('.mod-fil-fans').text()
items = doc('.card.m-panel.card9.weibo-member').items()
j=0  #@某人的次数
k=0  #获得点赞数
h=0  #获得评论数
m=0  #被转发数
info_list=[]
for item in items:
    info={
        'text':item.find(".weibo-text").text(),
        'likes':item.find(".m-icon.m-icon-like").siblings().text().replace('赞','0'),
        'forwards':item.find(".m-font.m-font-forward").siblings().text().replace('转发','0'),
        'comments':item.find(".m-font.m-font-comment").siblings().text().replace('评论','0'),
        'time':item.find(".time").text(),
        'from':item.find(".from").text().replace('来自 ',''),
        }
    info_list.append(info)
    if "@aaaYue啊"in info['text']:
        j+=1
    k+=int(info['likes'])
    h+=int(info['comments'])
    m+=int(info['forwards'])
print("用户id："+id_name)
print("微博基本信息：" +'\n'+ shadow.replace('\n',''))
print("自{}以来：\n共发微博{}条".format(info_list[-1]['time'],len(info_list)))
print("共@了用户'aaaYue啊'{}次,".format(j))
print("获得点赞数：{}条".format(k))
print("获得评论数：{}条".format(h))
print("获得转发数：{}条".format(m))


MONGO_URL='localhost'
MONGO_DB='weibo'
MONGO_COLLECTION=id_name
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
try:
    if db[MONGO_COLLECTION].insert(info_list):
        print("储存到MongoDB成功")
except Exception:
    print("储存到MongoDB失败")
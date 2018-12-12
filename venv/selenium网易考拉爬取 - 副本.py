from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from pyquery import PyQuery as pq
import time
import pymongo

broswer=webdriver.Chrome()
KEYWORD="祛痘"  ##可变关键字搜索不同产品
url="https://www.kaola.com/search.html?zn=top&key="+quote(KEYWORD)
broswer.get(url)
list=[]

def get_products():
    html = broswer.page_source
    doc = pq(html)
    items = doc('#searchbox .resultwrap .m-result .clearfix .goods').items()
    for item in items:
            product={
                'image':item.find('a .img .imgtag').attr('src'),
                'price':item.find('.cur').text().replace("¥",""),
                'marketprice':item.find('.marketprice').text().replace('\n','').replace("¥",""),
                'title':item.find('.titlewrap').text(),
                'shop':item.find('.selfflag').text(),
                'location':item.find('.proPlace.ellipsis').text(),
                'comment':item.find('.comments').text(),
                'saelsinfo':item.find('.saelsinfo').text()
            }
            list.append(product)
            print(product)
            save_to_mogo(product)
    jump_page()


def jump_page():
    try:
        submit=broswer.find_element_by_class_name('nextPage')###需要优化，找到方法定位该字段还包含href属性才行
        submit.click()
        time.sleep(3)
        get_products()
    except:
        print("jump_page wrong")

MONGO_URL='localhost'
MONGO_DB='wangyikaola'
MONGO_COLLECTION='products'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
def save_to_mogo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print("储存到MongoDB成功")
    except Exception:
        print("储存到MongoDB失败")

get_products()
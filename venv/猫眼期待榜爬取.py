import re
import requests
import json
import time
#获取服务器响应的html页
def get_page(url):
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    respose=requests.get(url,headers=header)
    if respose.status_code==200:
        return respose.text
    return None
#正则匹配所需内容
def parse_one_page(html):
    parttern=re.compile('<dd>.*?board-index.*?">(.*?)</i>.*?<p class="name">.*?title="(.*?)" data-act.*?<p class="star">'
                        '(.*?)</p><p class="releasetime">(.*?)</p>',re.S)
    items=re.findall(parttern,html)
    for item in items:
        yield{
            "排名":item[0],
            "片名":item[1],
            "主演":item[2][3:],
            "上映时间":item[3][5:]
        }
# 将内容写入文件
def write_to_file(content):
    with open ('result.txt',"a",encoding='utf-8')as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

for i in [0,10,20,30,40]:
    url="http://maoyan.com/board/6?offset="+str(i)
    html=get_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
    time.sleep(1)
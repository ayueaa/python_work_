import re
import requests
from pyquery import PyQuery as pq
import json
import pandas
from openpyxl import Workbook
urls="https://cre.mix.sina.com.cn/api/v3/get?callback=jQuery111108514137348190296_1544522533419&cateid=1o&cre=tianyi&mod=pcnews&merge=3&statics=1&length=15&up={}&down=0&tm=1544522528&action=1&top_id=AGuAG%2CAGdSk%2CADlUf%2CAGoCa%2CAGXJR%2CAGehQ%2CAGpSG%2CAGb7U%2CAH1W6%2CAGTby%2CAGOf9%2CAH5tQ%2CAH16A%2CAGNjD%2CAH1g3%2CAGtl0%2CAGoXn%2CAGdVH%2CAH62Z%2CAGryV&offset=0&ad=%7B%22rotate_count%22%3A100%2C%22platform%22%3A%22pc%22%2C%22channel%22%3A%22tianyi_pcnews%22%2C%22page_url%22%3A%22https%3A%2F%2Fnews.sina.com.cn%2F%22%2C%22timestamp%22%3A1544522534137%7D"
news_urls=[]
for i in range(1,11):
    url=urls.format(i) #获取每个分页url
    response=requests.get(url).text.rstrip(");\n").lstrip("jQuery111108514137348190296_1544522533419(")
    ld=json.loads(response)
    for ul in ld["data"]:
        news_urls.append(ul["url"])
print(len(news_urls))
print(news_urls)

results=[]
for content_url in  news_urls:
    result = {}
    content=requests.get(content_url)
    content.encoding="utf-8"
    doc=pq(content.text)
    author = doc(".date-source a").text()
    time= doc(".date").text()
    title= doc(".main-title").text()
    content = doc(".article").text()

    result["author"]=author
    result["time"]=time
    result["title"]=title
    result["content"]=content
    results.append(result)
    with open('news.txt','a',encoding='utf-8') as f:
        f.write('\n'.join([author,time,title,content]))
        f.write('\n'+'='*50+'\n')
print(results)
db=pandas.DataFrame(results)
print(db)
db.to_excel("news.xlsx")



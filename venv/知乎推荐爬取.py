import requests
from pyquery import PyQuery as pq
import re
url="https://www.zhihu.com/hot"
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
         'cookie':'_zap=d2091868-c46e-42d1-aca8-26d19894be6c; _xsrf=C3FWIBTixJhWYysxBy4VXcDdihzNkoLt; '
                  'd_c0="AHDiLgX7gQ6PTlmhPLb53zozfih920ntDvo=|1542021015"; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc;'
                  ' capsion_ticket="2|1:0|10:1542537444|14:capsion_ticket|44:'
                  'NDlmN2I4MzhjZmVlNGQzMGFhNWI0YmU2MGFkZDg0OTI=|f223446ec31aca28390f47c03d53ed40546ee344b3a48843a4d0345baf428a9d"; '
                  'z_c0="2|1:0|10:1542537450|4:z_c0|92:Mi4xSTUtekJRQUFBQUFBY09JdUJmdUJEaVlBQUFCZ0FsVk42bzdlWEFDRGQxQkFtc'
                  'llZaEhhR1lmV1lPdU9KRVNPVlBn|6a9119eb6a06aa3b4f658257f07a6f53c559fa847db6d47019fda33bd91e434f"; '
                  'tst=r; q_c1=1ac8876c96be405b9f3445397575d664|1542537452000|1542537452000; __utma='
                  '51854390.2128530113.1542537460.1542537460.1542537460.1; __utmb=51854390.0.10.1542537460;'
                  ' __utmc=51854390; __utmz=51854390.1542537460.1.1.utmcsr=zhihu.com|utmccn=(referral)|'
                  'utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20170815=1^3=entry_date=20170815=1'
         }
html=requests.get(url,headers=headers).text
doc=pq(html)
items=doc("section").items()
i=0
for item in items:
    question=item.find('h2').text()
    answer=item.find('p').text()
    hot=re.findall(r'<div class="HotItem-metrics HotItem-metrics--bottom".*?</svg>(.*?)<span',html,re.S)[i]
    with open('zhihu.txt','a',encoding='utf-8') as f:
        f.write('\n'.join([hot,question,answer]))
        f.write('\n'+'='*50+'\n')
    i+=1
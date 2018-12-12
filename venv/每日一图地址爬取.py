import re
import urllib.request
title_list=[]
url_info_list=[]
i = 844
while i > 840:
    url = "http://bing.plmeizi.com/show/"+str(i)
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    message = re.findall(r'<span id="title">(.*?)>>查看大图</a>',html,re.S)[0]
    title = re.findall(r'(.*?) ',message,re.S)[0]
    url_info = re.findall(r'<a href="(.*?)" target="_blank" id="picurl">',message,re.S)[0]
    title_list.append(title)
    url_info_list.append(url_info)
    i-=1
print(title_list,url_info_list)
j = len(url_info_list)
for k in range(0,j):
    url=url_info_list[k]
    page = urllib.request.urlopen(url)
    picture = page.read()
    with open('%s.jpg'%title_list[k],'wb') as f:
        f.write(picture)
    print("正在下载%s"%title_list[k] )
print("下载完成")
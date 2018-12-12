import requests
import re
url="https://www.ybdu.com/xiaoshuo/14/14727/"      #笔趣阁小说网
response=requests.get(url)
response.encoding="gbk"       #中文转译
html=response.text
title=re.findall(r'<meta property="og:title" content="(.*?)"/>',html)
ul_class=re.findall(r'<ul class="mulu_list">.*?</ul>',html,re.S)[0]
chapter_info_list=re.findall(r'<li><a href="(.*?)">(.*?)</a></li>',ul_class)
fb=open('%s.text'%title,'w',encoding='utf-8')  # 新建文本文件，命名等于title
for chapter_info in chapter_info_list:
    chapter_title=chapter_info[1]
    chapter_url = chapter_info[0]
    chapter_url='https://www.ybdu.com/xiaoshuo/14/14727/'+ chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = "gbk"
    chapter_html = chapter_response.text
    chapter_content = re.findall(r'<div id="htmlContent" class="contentbox">.*?<div class="ad00"><script>show_style\(\);</script></div>', chapter_html, re.S)[0]   #数据清洗
    chapter_content = chapter_content.replace("&nbsp;","")
    chapter_content = chapter_content.replace('<div id="htmlContent" class="contentbox">',"")
    chapter_content = chapter_content.replace('<div class="ad00"><script>show_style();</script></div>', "")
    chapter_content = chapter_content.replace("<br />","")
    fb.write(chapter_title)   #写入text文档
    fb.write(chapter_content)
    fb.write("\n")
    print(chapter_url)
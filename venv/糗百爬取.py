import requests
import re
import time
time_start=time.time()
page=1
joke_book=[]
#指定需要爬取的页数
while page<2:
    url="https://www.qiushibaike.com/hot/page/"+str(page)
    try:
        kv={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}
        response=requests.get(url,headers=kv)
        response.status_code
        response.encoding="utf-8"
        content=response.text
    except:
        print("连接错误")
    # 获取每条段子独立的连接（有些长段子主页面内显示不完全）
    hot_url=re.findall(r'<a href="/article/(\d*?)" target="_blank"',content,re.S)
    print("正在获取糗百热门--page %d--中所有段子链接..."%page)
    #次列表用于存放每个段子信息的字典
    i=1
    for adress in hot_url:
        single_url="https://www.qiushibaike.com/article/"+adress
        single_response = requests.get(single_url, headers=kv)
        single_response.status_code
        single_response.encoding = "utf-8"
        sl_content = single_response.text.replace("\n","")
        info_dict={}
        print("    正在获取 page {} 中第{}个段子信息".format(page,i))
        try:
            # 获取该段子正文
            main_text = re.findall(
                r'title="下一条"><div class="content">(.*?)</div></div><div class=\'page-nav-list\'>',
                sl_content,re.S)[0]
            main_text=main_text.replace("<br/>","")
            # 分别得到作者、点赞、评论数到列表
            extra_info = list(re.findall(
                r'target="_blank" title="(.*?)"><h2>.*?<i class="number">(.*?)</i> 好笑.*?</span>'
                r'<i class="number">(.*?)</i> 评论',sl_content, re.S)[0])
        except IndexError:
            print("    该页包含图片内容，重新获取下一条文本")
            continue
        if len(extra_info)==0:
            continue
        else:
            # 提取作者信息
            author_name=extra_info[0]
            # 提取点赞数
            praise_num=extra_info[1]
            #提取评论数
            comments_num=extra_info[2]
            # 提取神评论列表
            hot_comments = re.findall(r'<div class="main-text">(.*?)</div>', sl_content, re.S)
            info_dict["main_text"] = main_text
            info_dict["author"] = author_name
            info_dict["praise_num"] = praise_num
            info_dict["comments_num"] = comments_num
            info_dict["hot_comments"]=hot_comments
            joke_book.append(info_dict)
            with open("段子.txt","a",encoding="utf-8")as f:
                f.write("\n".join([main_text,author_name,praise_num,comments_num,str(hot_comments)]))
                f.write("="*50+"\n")

        i += 1
    page+=1
with open("qiubai.txt","w",encoding="utf-8")as f:
    f.write(str(joke_book))
print("\n爬取完毕，本次共获取{}页、{}条段子".format(page-1,len(joke_book)))
time_end=time.time()
print("总共耗时:",time_end-time_start)


def read_info(num):
    te = joke_book[num]
    return ("本条作者是：{}\n点赞数：{}    评论数：{}\n内容：{}\n神评论：{}"
          .format(te['author'], te['praise_num'], te['comments_num'], te['main_text'], te['hot_comments']))
while True:
    num=int(input("\n现在你想看哪条段子？（输入数字读取，输入q退出）："))
    try:
        if num!="q":
            print(read_info(num))
        else:
            break
    except:
        print("输入值有误，请重新输入")


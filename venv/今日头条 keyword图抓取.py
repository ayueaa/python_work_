import requests
from urllib.parse import urlencode

def get_pages(offset):
    headers={
    'referer': 'https://www.toutiao.com/search/?keyword=cos',
    'user - agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'x - requested -with': 'XMLHttpRequest',
    }
    params={
        'offset': offset,
        'format': 'json',
        'keyword': '雪山',
        'autoload': 'true',
        'count':'20',
        'cur_tab':'1',
        'from': 'search_tab',
    }
    url="https://www.toutiao.com/search_content/?"+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        print("访问错误")

def get_images(json):

    try:
        if json.get("data"):
            for item in json.get("data"):
                title=item.get("title")
                images=item.get("image_list")
                for image in images:
                    yield {
                        "image":"http:"+image.get('url').replace("list","large"),
                        "title":title
                    }
    except TypeError:
        print("该网址解析错误，下载失败")

import os
from hashlib import md5

def save_image(item):
    if not os.path.exists(item.get("title")):
        os.mkdir(item.get("title"))
    try:
        response=requests.get(item.get("image"))
        if response.status_code==200:
            file_path="{0}/{1}.{2}".format(item.get("title"),md5(response.content).hexdigest(),"jpg")
            if not os.path.exists(file_path):
                with open(file_path,'wb')as f:
                    f.write(response.content)
            else:
                print("Already Download",file_path)
    except requests.ConnectionError:
        print("Failed to Save Image")


from multiprocessing.pool import Pool

def main(offset):
    json=get_pages(offset)
    for item in get_images(json):
        print("正在下载")
        print(item)
        save_image(item)

GROUP_START=1
GROUP_END=2
if __name__=="__main__":
    pool=Pool()
    groups=([x*20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()




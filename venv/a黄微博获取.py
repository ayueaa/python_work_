from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
base_url="https://m.weibo.cn/api/container/getIndex?"
headers={
    'Host':'m.weibo.cn',
    'Referer': 'https://m.weibo.cn/p/2304133002577882_-_WEIBO_SECOND_PROFILE_WEIBO',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
id="4306714457223432"
def get_page():
    params={
        'uid': '2202955263',
        'luicode': '10000011',
        'lfid': '100103type = 1 & q = 十七十八一枝花',
        'containerid': '1076032202955263',
        'since_id': id,
    }
    url = base_url + urlencode(params)###解析错误，原因待查，改用下行原始方法操作
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print("Erro",e.args)
def get_since_id(json):
    if json:
        id = json.get('data').get('cardlistInfo').get("since_id")
    print(id)
def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item=item.get('mblog')
            weibo={}
            weibo['id']=item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['time'] = item.get('created_at')
            yield weibo
if __name__=='__main__':
    for i in range(1,2):   #第一页布局和网址不同 需要单独获取
        json=get_page()
        results=parse_page(json)
        for result in results:
            print(result)
        get_since_id(json)
        ###待完善内容储存功能、图片、视频功能、互动数据


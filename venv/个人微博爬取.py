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
def get_page(page):
    """params={
        'containerid': '2304133002577882_ - _WEIBO_SECOND_PROFILE_WEIBO',
        'page_type':'03',
        'page': page,
    }
    url = base_url + urlencode(params)"""###解析错误，原因待查，改用下行原始方法操作
    url = base_url + "containerid=2304133002577882_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page="+str(page)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print("Erro",e.args)

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
    for page in range(2,23):   #第一页布局和网址不同 需要单独获取
        json=get_page(page)
        results=parse_page(json)
        for result in results:
            print(result)
        ###待完善内容储存功能、图片、视频功能、互动数据


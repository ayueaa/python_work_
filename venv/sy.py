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
url = base_url + "containerid=2304133002577882_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page=3"
try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json=response.json()
except requests.ConnectionError as e:
    print("Erro",e.args)

def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        print(type(items))###
        print(items[0].get('card_type'))####
        for item in items:
            print(item)###
            item=item.get('mblog')
            weibo={}
            weibo['id']=item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['time'] = item.get('created_at')
            yield weibo
if __name__=='__main__':
    for page in range(3,4):
        results=parse_page(json)
        for result in results:
            print(result)
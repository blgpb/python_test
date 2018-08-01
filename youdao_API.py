
import urllib
import random

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.2) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
]
user_agent = random.choice(user_agent_list)

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
key = input('Please input the English that want to be translated:')

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest'
}
formdata = {
    'i': key,
    'from':'en',
    'to':'zh-CHS',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1533094728579',
    'sign':'3f08610d3ea541240a2964b58f9f6ee3',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'false'
}

data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')

request = urllib.request.Request(url, data = data)
request.add_header('User-Agent', user_agent)

translation = str(urllib.request.urlopen(request).read(), 'utf-8')
#print(translation)

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str = content_str+i
    return content_str

basic_str = format_str(translation)
print('The result of translation by youdao:'+basic_str)
import urllib
import random

url = 'http://www.baidu.com/s'
keyword = input('Please input the keyword that want to be searched:')

wd = {'wd' : keyword}
wd = urllib.parse.urlencode(wd)

fullurl = url + '?' + wd

print(fullurl)

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.2) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
]

user_agent = random.choice(user_agent_list)


request = urllib.request.Request(fullurl)

request.add_header('User-Agent', user_agent)
print(request.get_header('User-agent'))

response = urllib.request.urlopen(request)

print(str(response.read(), 'utf-8'))

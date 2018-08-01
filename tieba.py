import urllib

def loadPage(url, filename):
    """
    obtain the html according to the url
    :param url: the url that need to be crawled
    :return:
    """
    print('Downloading...')
    headers = {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}
    request = urllib.request.Request(url, headers = headers)
    html = str(urllib.request.urlopen(request).read(), 'utf-8')
    writePage(html, filename)

def writePage(html, filename):
    """
    write the html to local file
    :param html: the html that returned by the server
    :return:
    """
    print('Saving   ' + filename)
    with open(filename, 'w') as f:
        f.write(str(html))
    print('-'*50)

def tiebaSpider(url, beginPage, endPage):
     """
     process the url of every tieba page
     :param url:
     :param beginPage:
     :param endPage:
     :return:
     """
     for page in range(beginPage, endPage + 1):
         pn = (page - 1) * 50
         filename = 'page' + str(page) + '.html'
         fullurl = url + '&pn=' + str(pn)
         #print(fullurl)
         html = loadPage(fullurl, filename)
         print(html)

if __name__ == '__main__':
    kw = input('Please input the tieba name:')
    beginPage = int(input('Please input the begin page:'))
    endPage = int(input('Please input the end page:'))

    url = 'http://tieba.baidu.com/f?'
    key = urllib.parse.urlencode({'kw': kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)

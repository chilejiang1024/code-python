# encoding:utf-8

import urllib.request as request

r = request.urlopen('http://www.baidu.com')
print(r.read())


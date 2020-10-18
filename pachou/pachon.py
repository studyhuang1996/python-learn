from urllib import request,parse

url = 'http://www.baidu.com/'
response = request.urlopen(url)

#print(response.read().decode("utf-8"))

import socket
import urllib
try:
    response2 = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('time out')
        
import requests

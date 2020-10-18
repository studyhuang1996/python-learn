import requests

url = 'http://httpbin.org/get'

data={'key':'value','abc':"123"}

#get请求
response = requests.get(url,data)

print(response.text)

#post请求

url2 = 'http://httpbin.org/post'
response02 = requests.post(url2,data)
print(response02.json())
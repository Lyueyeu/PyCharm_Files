# coding= utf-8
# 这个可以用以在JSON传参的时候的情况，先把接口参数参数化之后再传递，现在需要考虑的是怎么将的参数传递到这边来
import requests
# 发送请求
print(requests.get('https://github.com/timeline.json'))
r = requests.post("http://httpbin.org/post")
print(r)
# 为URL传递参数
payload = {'key1': 'value1', 'key2': 'value2'}
r1 = requests.get("http://httpbin.org/get", params=payload)
print(r1)
print(r1.url)
# 获取响应的内容
r2 = requests.get('https://github.com/timeline.json')
print(r2)
print(r2.text)
# 二进制响应内容
print(r2.content)
# from PIL import Image
# from StrinIO import StringIO
# i = Image.open(StringIO(r.content))

# JSON响应内容
print(r2.json())

# 原始响应内容
print(r2.raw)
print(r2.raw.read(10))
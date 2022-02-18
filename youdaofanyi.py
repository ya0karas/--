from urllib import response
import urllib.parse
import urllib.request
import json

content = input('请输入内容：')

url = ' https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {'i' : content, 'from' : 'AUTO', 'to' :'AUTO', 'smartresult' : 'dict', 'client':'fanyideskweb', 'doctype':'json', 'version': '2.1', 'keyfrom': 'fanyi.web'}
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

target = json.loads(html)
print('翻译结果是：%s' % target['translateResult'][0][0]['tgt'])
#print('翻译结果：%S' % (target['translateResult']))

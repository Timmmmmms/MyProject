# -*- coding:utf-8 -*-
# 合成文本长度必须小于1024字节，如果本文长度较长，可以采用多次请求的方式。文本长度不可超过限制
from aip import AipSpeech

# 你的APPID
APP_ID = '11861586'
API_KEY = 'HoC8vDjZmjWI9GLHh2t9XYan'
SECRET_KEY = 'iqPnm6CWKck1rRTwaECSnoq6q6ldGx1r'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

text = input("请输入你要合成的文字：")
result = client.synthesis(text,'zh',1,{'vol':5,'spd':10,'pit':10,'per':3})
# 识别正确返回语音二进制，错误则返回dict
if not isinstance(result,dict):
    with open('auido.amr','wb') as f:
        f.write(result)
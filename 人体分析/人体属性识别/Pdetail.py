# -*- coding:utf-8 -*-
from aip import AipBodyAnalysis
import time

# APPID
APP_ID = '11828915'
API_KEY = 'TxGkNH961xrF41oxeP86pdKr'
SECRET_KEY = 'IKAacd4z9CoPp06RaWlwgYqe3g5TfelN'

client = AipBodyAnalysis(APP_ID,API_KEY,SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

# 可选参数
options = {}
options['type'] = 'gender,age,headwear,glasses,orientation'

# 调用人体属性识别
t1 = time.time()
details = client.bodyAttr(image,options)
# print(details['person_info'][0]['attributes']['gender']['name'])
# print(details['person_info'][0]['attributes']['glasses']['name'])
# print(details['person_info'][0]['attributes']['age']['name'])
# print(details['person_info'][0]['attributes']['headwear']['name'])
# print(details['person_info'][0]['attributes']['orientation']['name'])
for i in ['gender','glasses','age','headwear','orientation']:
    print(details['person_info'][0]['attributes'][i]['name'])
t2 = time.time()
print(t2-t1)

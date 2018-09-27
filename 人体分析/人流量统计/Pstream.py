# -*- coding:utf-8 -*-
# 对于输入的一张图片（可正常解码，且长宽比适宜），识别和统计图像中的人体个数，以俯拍角度为主要识别视角
from aip import AipBodyAnalysis

# APPID
APP_ID = '11828915'
API_KEY = 'TxGkNH961xrF41oxeP86pdKr'
SECRET_KEY = 'IKAacd4z9CoPp06RaWlwgYqe3g5TfelN'

client = AipBodyAnalysis(APP_ID,API_KEY,SECRET_KEY)


# 读取图片
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

image = get_file_content('example9.jpg')

# 调用人流量统计
print("人数有："+str(client.bodyNum(image)['person_num']))


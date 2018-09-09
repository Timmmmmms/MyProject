import requests
import json
import os

def get_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url,headers=headers)
    # ~ print(res.text)
    return res
    
def get_rank(res): 
    result = []   
    obj = json.loads(res.text)
    for i in obj['data']['list']:
        detail = {}
        detail['rank'] = i['rank']
        detail['uname'] = i['uname']
        detail['uface'] = i['uface']
        result.append(detail)
        # ~ print(detail['uface'])
    return result

def wait_index(index):
    if not os.path.exists(index):
        os.mkdir(index)
    if not os.path.exists(index+'/Image'):
        os.mkdir(index+'/Image')
    url = "https://api.live.bilibili.com/rankdb/v1/Rank2018/getWebTop?date={}&type=master_vitality_2018&area_id=1&page=1&is_trend=1&page_size=20".format(index)
    print(url)
    res = get_url(url)
    result = get_rank(res)
    f = open(index+'/rank.txt','w',encoding="utf-8")
    # 将排名写入txt文件
    for i in result:
        f_info = str(i['rank'])+" "+i['uname']
        f.write(f_info+"\n")
    # 将各排名up主头像下载到Image文件夹
        img_res = get_url(i['uface'])
        with open("./"+index+"/"+"Image/{}.jpg".format(f_info),'ab') as p:
            p.write(img_res.content)

def main():
    indexs = ['day','week','month']
    for index in indexs:
        wait_index(index)
        
if __name__ == "__main__":
    main()

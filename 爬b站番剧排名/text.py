import requests
import bs4
import json

def open_url(url):
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url,headers=headers)
    return res

def get_detail(res):
    bsobj = bs4.BeautifulSoup(res.text,'html.parser')
    targets = bsobj.find('ul',class_="rank-list bangumi")
    result =[]
    for i in targets:
        item = {}
        item['rank'] = i.find('div',class_="num").text
        item['name'] = i.find('div',class_="info").a.text
        item['num'] = i.find('div',class_="detail").find_all('span',class_="data-box")[1].text
        item['pts'] = i.find('div',class_="pts").div.text
        # ~ print(str(rank)+" "+name+" "+"追番人数："+ str(num)+" "+"综合得分："+pts)
        result.append(item)
    # ~ print(result)
    return result
    
def main():
    url = "https://www.bilibili.com/ranking/bangumi/13/0/7"
    res = open_url(url)
    # ~ with open("te.txt","w",encoding="utf-8") as f:
        # ~ f.write(res.text)
    result = get_detail(res)
    f = open("番剧排名.txt",'w',encoding='utf-8')
    for i in result:
            f.write(str(i['rank'])+" "+i['name']+" "+"追番人数："+ i['num']+" "+"综合得分："+i['pts']+"\n")

if __name__ =="__main__":
    main()

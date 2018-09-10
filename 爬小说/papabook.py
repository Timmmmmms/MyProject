import requests
import bs4
import re

def url_open(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url,headers=headers)
    # ~ print(res.content.decode('gbk'))
    return res

def get_imformation(res):
    target = []
    soup = bs4.BeautifulSoup(res.content,"html.parser")
    obj = soup.find('div',class_="clearfix dirconone").find_all('li')
    for i in obj:
        subobj = {}
        subobj['name'] = i.a.text
        subobj['html'] = i.a.get("href")
        # ~ print(i.a.get("href"))
        target.append(subobj)
    return target

def call_text(html):
    res = url_open(html)
    html = res.content.decode('gbk')
    req = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
    # S多行匹配的意思
    req = re.compile(req,re.S)
    rq = re.findall(req,html)
    # 替换不需要的字符
    rq = rq[0].replace('&nbsp;','')
    rq = rq.replace('<br />','')
    return rq
def download(target):
    for i in target:
        with open("./book/{}.txt".format(i['name']),'w') as f:
            f.write(call_text(i['html']))
            print(i['html'])
            # ~ call_text(i['html'])
            
        
def main():
    url ="http://www.quanshuwang.com/book/44/44683"
    res = url_open(url)
    target = get_imformation(res)
    download(target)
    
if __name__ == "__main__":
    main()

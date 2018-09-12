import requests
from lxml import etree 

def open_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url,headers=headers)
    return res

def get_attr(res):
    # 把网页初始化
    html = etree.HTML(res.text)
    # Xpath text()选择文本
    names = html.xpath('//div[@class="company-text"]/h3[@class="name"]//text()')
    jobs = html.xpath('//h3[@class="name"]/a/div[@class="job-title"]//text()')
    moneys = html.xpath('//h3[@class="name"]/a/span[@class="red"]//text()')
    items = []
    for i in range(len(names)):
        attr = {}
        attr['name'] = names[i]
        attr['job'] = jobs[i]
        attr['money'] = moneys[i]
        items.append(attr)
    return items
    
def main():
    for page in range(11):
        url = "https://www.zhipin.com/c101280100-p100109/?page={}&ka=page-{}".format(page,page)
        res = open_url(url)
        items = get_attr(res)
        with open('data.txt','a',encoding='utf-8') as f:
            for i in items:
                f.write('name:'+i['name']+'\t'+'job:'+i['job']+'\t'+'money:'+i['money']+'\n')
                
    
if __name__ =="__main__":
    main()

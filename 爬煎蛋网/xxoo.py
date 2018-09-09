import requests
import bs4

def open_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url,headers=headers)
    print(res.text)
    return res

def get_url(res):
    soup = bs4.BeautifulSoup(res.content.decode('gbk','ignore'),'html.parser')
    obj = soup.find_all('div',class_="text")
    print(obj)
    for i in obj:
        img_addr = i.get('href')
        print(img_addr)
    
def main():
    url = "http://jandan.net/ooxx"
    res = open_url(url)
    result = get_url(res)

if __name__ == "__main__":
    main()

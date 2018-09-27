import requests
import re

def url_open(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    res = requests.get(url, headers=headers)
    return res

def get_p(res):
    pattern = re.compile("data-pin-media=\\\\\"(.*?)\?")        # re中反斜杠用\\\\ 或 r"data-pin-media=\\\"(.*?)\?"
    photo_addr_list = re.findall(pattern, res.text)
    return photo_addr_list
    
def get_photo_downaddr(photo_addr_list,width,height):
    urls = []
    for addr in photo_addr_list:
        url = addr + "?dl&fit=crop&crop=entropy&w=" +str(width) + "&h=" + str(height)
        urls.append(url)
    return urls

def download_pic(url,name):
    res = url_open(url)
    with open("./photo/"+ str(name) + ".jpeg","ab") as f:
        f.write(res.content)


def main():
    name = 1
    width = 1920
    height = 1080
    page = 1                # 当前页数
    crawl_page_num = 10     # 爬取的页数
    
    while page < crawl_page_num:
        base_url = "https://www.pexels.com/?dark=true&format=js&page=" + str(page)
        res = url_open(base_url)
        photo_addr_list = get_p(res)
        pic_urls = get_photo_downaddr(photo_addr_list,width,height)
        for url in pic_urls:
            download_pic(url,name)
            name +=1
        page += 1


if __name__ == "__main__":
    main()

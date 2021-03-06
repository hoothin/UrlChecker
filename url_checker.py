#-*- coding: utf-8 -*- 
import random
import sys
import re
import threading, queue
import html
import socket
import requests
from datetime import *
from requests.adapters import HTTPAdapter
from urllib.parse import urlparse

socket.setdefaulttimeout(10)
requests.packages.urllib3.disable_warnings()
url_queue = queue.Queue()
threading_num = 50
count = 0
survival_urls = {}
broken_urls = {}
jsError_urls = {}
useragent_list = [
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1) Gecko/20061010 Firefox/2.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1 ; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre",
    "Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60",
    "Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4062; en; U; ssr)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr; rv:1.9.2.4) Gecko/20100523 Firefox/3.6.4 ( .NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5"
]


def Banner():
    print("""
 █    ██  ██▀███   ██▓     ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
 ██  ▓██▒▓██ ▒ ██▒▓██▒    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██  ▒██░▓██ ░▄█ ▒▒██░    ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▓▓█  ░██░▒██▀▀█▄  ▒██░    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒▒█████▓ ░██▓ ▒██▒░██████▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░░░ ░ ░   ░░   ░   ░ ░   ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
   ░        ░         ░  ░░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                          ░                       ░                               
                                                           Power by Hoothin  v0.1
    """)


def get_headers(url):
    res = urlparse(url)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': random.choice(useragent_list),
        'Accept-Encoding': 'identity',#'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        "Referer": res.scheme + "://" + res.netloc,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return headers


def get_url(urls_txt):
    with open(urls_txt, 'r') as f:
        urls_list = f.readlines()
    return urls_list


def url_check():
    global survival_urls
    global broken_urls
    global jsError_urls
    while not url_queue.empty():

        global count
        url = url_queue.get()

        url = url.strip()
        headers = get_headers(url)
        # print(url)
        try:
            #if "http" not in url and len(url) != 0  :
            #    url = "http://"+ url
            s = requests.Session()
            s.mount('http://', HTTPAdapter(max_retries=3))
            s.mount('https://', HTTPAdapter(max_retries=3))
            startTime = datetime.now()
            response = s.get(url, headers=headers, timeout=5, verify=False, allow_redirects=True, stream=True)#no ssl, no 301
            outStr = str(response.status_code)
            # survival_urls[url] = response.status_code
            if ("video" in response.headers['content-type'] or 
                "audio" in response.headers['content-type'] or 
                "octet-stream" in response.headers['content-type'] or
                "binary" in response.headers['content-type'] or
                "mepgURL" in response.headers['content-type'] or
                "mpegurl" in response.headers['content-type'] or
                "mpegURL" in response.headers['content-type']):
                response.connection.close()
                # outStr = outStr + "\t非网页：" + response.headers['content-type']
            else:
                if 200 <= response.status_code <= 206:
                    endTime = datetime.now()
                    span = (endTime-startTime).total_seconds()
                    response.encoding = response.apparent_encoding
                    content = response.text
                    outStr = str(span) + " seconds\t" + outStr
                    title = re.findall('<title>(.+)</title>', content)
                    if title:
                        outStr = outStr + "\t" + html.unescape(title[0])
                        if "江苏反诈公益宣传" in title:
                            jsError_urls[urlparse(url).netloc] = 1
                    survival_urls[url] = outStr
                else:
                    broken_urls[urlparse(url).netloc] = outStr
            print(url + "\t" + outStr)
        except Exception as e:
            broken_urls[urlparse(url).netloc] = "error"
            print(url + "\t网站失效")
        count += 1
        print("已检测：" + str(count), end="\r")
        url_queue.task_done()

def write_url():
    with open("result.txt", "w+", encoding='utf-8') as f:
        for url, status_code in survival_urls.items():
            f.write(url + "\t" + str(status_code) + "\n")
    with open("urlBroken.txt", "w+", encoding='utf-8') as f:
        for url, status_code in broken_urls.items():
            f.write(url + "\n")
    with open("urlJsError.txt", "w+", encoding='utf-8') as f:
        for url, status_code in jsError_urls.items():
            f.write(url + "\n")

def threading_start(urls_list):
    for url in urls_list:
        url = url.strip()
        if (len(url) == 0 or
            "m3u8" in url):
            continue
        url_queue.put(url)
    threads = []
    for _ in range(10):
        c = threading.Thread(target=url_check)
        threads.append(c)
        c.setDaemon(True)
    for t in threads:
        t.start()

    url_queue.join()


def urls_check(urls_txt):
    if "http" in urls_txt:
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))
        res = s.get(urls_txt, timeout=5)
        res.encoding = res.apparent_encoding
        urls_list=re.findall('https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', res.text)
        threading_start(urls_list)
        write_url()
        return 
    urls_list = get_url(urls_txt)
    threading_start(urls_list)
    write_url()

if __name__ == '__main__':
    Banner()

    try:
        urls_txt = sys.argv[1]
        urls_check(urls_txt)
    except Exception as e:
        print(e)
        print("python3 url_checker.py url.txt\n OR\npython3 url_checker.py http://xxx.com/x.txt")

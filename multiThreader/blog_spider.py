# @Author: eveleaf
# @Date: 2024-07-31 11:59
# @LastEditTime: 2024-07-31 12:01
# @Description:

import requests
from bs4 import BeautifulSoup
from queue import Queue

urls = [f"https://www.cnblogs.com/#p{i}" for i in range(1, 51)]


def craw(url):
    r = requests.get(url)
    # print(url, len(r.text))
    return r.text


def parse(html):
    # xml网页，解释器
    soup = BeautifulSoup(html, "html.parser")
    # 查找所有的tag列表，按tag名和class_属性
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]


if __name__ == "__main__":
    for result in parse(craw(urls[0])):
        print(result)

from typing import List
from collections import Counter
import requests
import time
import threading
from bs4 import BeautifulSoup
import blog_spider


def single_thread(urls):
    """单线程

    Arguments:
        urls -- url列表
    """
    start = time.time()
    for url in urls:
        blog_spider.craw(url)
    end = time.time()
    print(f"single thread cost: {end-start} seconds")


def multi_thread(urls):
    """多线程爬虫

    Arguments:
        urls -- url列表
    """
    start = time.time()
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=blog_spider.craw, args=(url,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        # 该线程任务结束后，任务才进行
        thread.join()
    end = time.time()
    print(f"multi thread cost: {end-start} seconds")

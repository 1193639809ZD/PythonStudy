from typing import List
from collections import Counter
import requests
import time
import threading
from bs4 import BeautifulSoup


def single_thread(urls):
    start = time.time()
    for url in urls:
        craw(url)
    end = time.time()
    print(f"single thread cost: {end-start} seconds")


def multi_thread(urls):
    start = time.time()
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=craw, args=(url,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        # 该线程任务结束后，任务才进行
        thread.join()
    end = time.time()
    print(f"multi thread cost: {end-start} seconds")

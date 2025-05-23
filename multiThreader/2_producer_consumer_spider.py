# @Author: eveleaf
# @Date: 2024-07-31 12:35
# @LastEditTime: 2024-07-31 12:43
# @Description:

import blog_spider
from queue import Queue
import threading
import random
import time


def do_craw(url_queue, html_queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(
            threading.current_thread().name,
            f"craw {url}",
            f"url_queue.size={url_queue.qsize()}",
        )
        time.sleep(random.randint(1, 2))


def do_parse(html_queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(
            threading.current_thread().name,
            f"results.size {len(results)}",
            f"html_queue.size={html_queue.qsize()}",
        )
        time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    url_queue = Queue()
    html_queue = Queue()

    for url in blog_spider.urls:
        url_queue.put(url)

    for idx in range(3):
        t = threading.Thread(
            target=do_craw, args=(url_queue, html_queue), name=f"craw{idx}"
        )
        t.start()

    font = open("2_data.txt", "w")
    for idx in range(2):
        t = threading.Thread(
            target=do_parse, args=(html_queue, font), name=f"parse{idx}"
        )
        t.start()

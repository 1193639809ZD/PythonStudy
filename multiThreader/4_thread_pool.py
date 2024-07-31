# @Author: eveleaf
# @Date: 2024-07-31 16:31
# @LastEditTime: 2024-07-31 16:37
# @Description: 线程池

import concurrent.futures
import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # 按顺序遍历
    # for future, url in futures.items():
    #     print(url, future.result())

    # 按完成顺序遍历
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())

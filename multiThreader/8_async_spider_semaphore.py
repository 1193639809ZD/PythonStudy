# @Author: eveleaf
# @Date: 2024-07-31 20:07
# @LastEditTime: 2024-07-31 20:08
# @Description: 信号量异步任务

import asyncio
import aiohttp
import blog_spider
from time import time

# 信号量机制，用于控制并发度
semaphore = asyncio.Semaphore(10)


async def async_craw(url):
    async with semaphore:
        print("craw url: ", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                print(f"craw url: {url}, {len(result)}")
                await asyncio.sleep(5)


loop = asyncio.get_event_loop()

tasts = [loop.create_task(async_craw(url)) for url in blog_spider.urls]

start = time()
loop.run_until_complete(asyncio.wait(tasts))
end = time()
print(f"async costs: {end-start} seconds")

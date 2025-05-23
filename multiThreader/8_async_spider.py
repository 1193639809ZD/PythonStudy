# @Author: eveleaf
# @Date: 2024-07-31 19:53
# @LastEditTime: 2024-07-31 19:53
# @Description:异步协程

import asyncio
import aiohttp
import blog_spider
from time import time


async def async_craw(url):
    print("craw url: ", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")


loop = asyncio.get_event_loop()

tasts = [loop.create_task(async_craw(url)) for url in blog_spider.urls]

start = time()
loop.run_until_complete(asyncio.wait(tasts))
end = time()
print(f"async costs: {end-start} seconds")

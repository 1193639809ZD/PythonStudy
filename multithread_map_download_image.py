# @Author: eveleaf
# @Date: 2024-08-02 17:02
# @LastEditTime: 2024-08-02 19:13
# @Description:


import requests
from time import time
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import argparse
import json


def download_image(image_url):
    save_path = Path(args.output).joinpath(Path(image_url).name)
    if save_path.exists():
        return (image_url, True)
    # 线程有自己的栈区，出现错误，不会抛到主线程，需要在函数中做错误处理
    try:
        r = requests.get(image_url, timeout=args.timeout)
    except:
        # 如何打印错误类型
        # print(f"{image_url}: passed")
        return (image_url, False)

    image = Image.open(BytesIO(r.content))
    image.save(save_path)
    # print(f"{image_url}: download")
    return (image_url, True)


if __name__ == "__main__":
    # 命令行参数
    parse = argparse.ArgumentParser(description="网络图片多线程下载脚本")
    parse.add_argument(
        "--output", default="/mnt/c/MyDataset/multi-thread1", help="输出文件夹"
    )
    parse.add_argument("--timeout", default=3, help="requests连接最大时间")
    parse.add_argument("--max_workers", default=8, help="最大线程数")
    args = parse.parse_args()

    # 获取图片的url列表
    mas_url = (
        "https://www.cs.toronto.edu/~vmnih/data/mass_buildings/train/sat/index.html"
    )
    r = requests.get(mas_url)
    soup = BeautifulSoup(r.text, "html.parser")
    image_urls = [item["href"] for item in soup.find_all("a")]

    # 根据图片url列表，将图片下载到输出文件夹
    if not Path(args.output).exists():
        Path(args.output).mkdir(parents=True)
    start = time()
    # 问题1，如何判断所有任务均完成，pool在什么情况下释放
    with ThreadPoolExecutor(max_workers=args.max_workers) as pool:
        results = pool.map(download_image, image_urls)
        for image_url, flag in results:
            print(f"{image_url}: {flag}")
    end = time()
    print(f"multi thread cost:{end-start} seconds")

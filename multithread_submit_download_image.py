# @Author: eveleaf
# @Date: 2024-07-30 09:40
# @LastEditTime: 2024-08-02 19:46
# @Description: 网络图片多线程下载脚本


import requests
from time import time
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import argparse


def download_image(image_url, output_dir):
    save_path = Path(output_dir).joinpath(Path(image_url).name)
    if save_path.exists():
        return True
    # 线程有自己的栈区，出现错误，不会抛到主线程，需要在函数中做错误处理
    try:
        r = requests.get(image_url, timeout=args.timeout)
    except:
        # print(f"{image_url}: passed")
        return False
    image = Image.open(BytesIO(r.content))
    image.save(save_path)
    # print(f"{image_url}: download")
    return True


if __name__ == "__main__":
    # 命令行参数
    parse = argparse.ArgumentParser(description="网络图片多线程下载脚本")
    parse.add_argument(
        "--output", default="/mnt/c/MyDataset/multi-thread", help="输出文件夹"
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
    start = time()
    # 使用with管理上下文，当全部任务完成后，自动关闭线程
    with ThreadPoolExecutor(max_workers=args.max_workers) as pool:
        results = {}
        for image_url in image_urls:
            result = pool.submit(download_image, image_url, args.output)
            results[result] = image_url
        for result in as_completed(results):
            print(f"{results[result]}: {result.result()}")
        pool.shutdown()
    end = time()
    print(f"multi thread cost:{end-start} seconds")

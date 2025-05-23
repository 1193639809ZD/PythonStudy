# @Author: eveleaf
# @Date: 2024-07-31 19:13
# @LastEditTime: 2024-07-31 19:15
# @Description:多进程

import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math
import time

# 单个任务计算时间长，可以使用多进程  ==> 另一个问题，单程序计算时间短，但是任务多会导致时间消耗变大，应该是由于同步进程造成的，如何解决
PRIMES = [112500] * 100


def function(n):
    for i in range(1, n):
        res = n % i
    return


def single_thread():
    for number in PRIMES:
        function(number)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(function, PRIMES)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(function, PRIMES)


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print(f"single thread costs:{end-start} seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print(f"multi thread costs:{end-start} seconds")

    start = time.time()
    multi_process()
    end = time.time()
    print(f"multi process costs:{end-start} seconds")

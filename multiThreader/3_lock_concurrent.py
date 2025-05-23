# @Author: eveleaf
# @Date: 2024-07-31 14:48
# @LastEditTime: 2024-07-31 14:53
# @Description:

import threading
import time


class Account:
    def __init__(self, balance) -> None:
        self.balance = balance


# 获取线程锁
lock = threading.Lock()


def draw(account, amount):
    # lock 同步
    with lock:
        if account.balance >= amount:
            # 线程阻塞，会导致切换线程，必定发生错误
            # time.sleep(0.1)
            print(threading.current_thread().name, "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name, f"余额{account.balance}")
        else:
            print(threading.current_thread().name, "取钱失败，余额不足")


if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(target=draw, args=(account, 800), name="ta")
    tb = threading.Thread(target=draw, args=(account, 800), name="tb")

    ta.start()
    tb.start()

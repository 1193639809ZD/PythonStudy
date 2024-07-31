# @Author: eveleaf
# @Date: 2024-07-31 16:55
# @LastEditTime: 2024-07-31 17:00
# @Description:使用多线程加速web服务

import json
import flask
import time
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
# 创建一个全局的线程池
pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.1)
    return "db result"


def read_api():
    time.sleep(0.1)
    return "api result"


@app.route("/")
def index():
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return json.dumps(
        {
            "result_file": result_file.result(),
            "resutl_db": result_db.result(),
            "result_api": result_api.result(),
        }
    )


if __name__ == "__main__":
    app.run()

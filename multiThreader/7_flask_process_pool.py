# @Author: eveleaf
# @Date: 2024-07-31 19:37
# @LastEditTime: 2024-08-19 14:44
# @Description:

# @Author: eveleaf
# @Date: 2024-07-31 19:37
# @LastEditTime: 2024-08-19 14:48
# @Description:多进程加速网页服务

import json
import flask
from concurrent.futures import ProcessPoolExecutor
import math

app = flask.Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == "__main__":
    # 无法放入main函数外面
    process_pool = ProcessPoolExecutor()
    app.run()

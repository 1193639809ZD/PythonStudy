"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2025-03-15 18:46:54
lastModified:  2025-03-15 18:46:55
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        # 遍历价格数组，从第1天开始比较
        for i in range(1, len(prices)):
            # 如果当前价格高于前一天价格，就卖出赚取差价
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit

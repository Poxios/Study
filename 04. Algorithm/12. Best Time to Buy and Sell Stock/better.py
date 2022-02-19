import sys
from typing import Dict, List

# Think in real life.
# Buy on low, sell on high.
# first, buy on lowest point.
# second, we know all scenario, so don't be scare of calculating min, max all times

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit

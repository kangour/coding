import unittest
import sys
from topic import logger


class Coins(unittest.TestCase):
    def coins(self, coins: list, amount: int):
        """暴力递归，当前硬币数量（1）加上子问题硬币数量"""

        res = sys.maxsize

        for coin in coins:
            # 选择当前硬币
            remain_amount = amount - coin

            # 刚好凑够，直接返回
            if remain_amount == 0:
                return 1

            # 币值超了，跳过
            if amount < 0:
                continue

            # 递归计算余额的硬币数量
            sub_problem = self.coins(coins, remain_amount)

            # 子问题中，没有解，跳过
            if sub_problem == -1:
                continue

            # 有解，子问题硬币数量加上已选的一个硬币
            res = min(res, sub_problem) + 1

        return res if res != sys.maxsize else -1

    def test(self):
        coins = [1, 2, 5]
        amount = 11

        res = self.coins(coins, amount)
        logger.info(f"最小兑换数量: {res}")

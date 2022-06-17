import unittest
import sys
from topic import logger


class Coins(unittest.TestCase):
    """
    结题顺序：
    1。 自上而下的暴力递归
    2。 自上而下的暴力递归 + 备忘录
    3。 自下而上的动态规划迭代
    """

    def __init__(self, *args, **kwargs):
        super(Coins, self).__init__(*args, **kwargs)
        self.amount_note = {}

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

    def coins_note(self, coins: list, amount: int):
        """在暴力递归的基础上，添加备忘录，记录已经计算过的金额和对应的数量，避免重复计算"""

        if amount == 0:
            return 0

        if amount < 0:
            return -1

        # 从备忘录取走数据
        if amount in self.amount_note:
            # logger.info(f"{self.amount_note} {amount} = {self.amount_note[amount]}")
            return self.amount_note[amount]

        res = sys.maxsize

        for coin in coins:
            # 选择当前硬币
            remain_amount = amount - coin

            # 刚好凑够，直接返回
            if remain_amount == 0:
                res = 1
                break

            # 币值超了，跳过
            if amount < 0:
                continue

            # 递归计算余额的硬币数量
            sub_problem = self.coins_note(coins, remain_amount)

            # 子问题中，没有解，跳过
            if sub_problem == -1:
                continue

            # 有解，子问题硬币数量加上已选的一个硬币
            res = min(res, sub_problem) + 1

        res = res if res != sys.maxsize else -1

        # 把结果存入备忘录
        self.amount_note[amount] = res

        return res

    @staticmethod
    def coins_dp(coins, amount):
        """DP 数组自底向上的迭代计算"""
        """求解 amount，dp 数组最大索引是 amount，故数组数量是 amount + 1 个"""
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        # 自底向上的找出子问题的可行解，得到每个解的最小数量，最终得到的就是最优解
        for _amount in range(amount + 1):
            # 穷举遍历每一个硬币，并对比所有可行解，找出最优解
            for coin in coins:

                sub_amount = _amount - coin
                if sub_amount < 0:
                    continue

                # 子问题的解，在 dp[sub_amount] 当中。
                dp[_amount] = min(dp[_amount], dp[sub_amount] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1

    def test(self):
        coins = [1, 2, 5]
        amount = 11

        res = self.coins(coins, amount)
        logger.info(f"最小兑换数量: {res}")

    def test_note(self):
        coins = [1, 2, 5]
        amount = 100

        res = self.coins_note(coins, amount)
        logger.info(f"最小兑换数量: {res}")

    def test_dp(self):
        coins = [1, 2, 5]
        amount = 100

        res = self.coins_dp(coins, amount)
        logger.info(f"最小兑换数量: {res}")

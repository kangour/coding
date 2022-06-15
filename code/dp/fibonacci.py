import unittest
from code import logger


class Fibonacci(unittest.TestCase):
    def fib(self, n: int):
        if n in [0, 1]:
            return n
        return self.fib(n - 1) + self.fib(n - 2)  # 调了两次递归，造成重复的计算，可以用动态规划思想优化

    @staticmethod
    def fib_note(n: int):
        """改良的斐波那契，用备忘录记录上一步的结果，避免重复计算"""
        if n in [0, 1]:
            return n
        a, b = 0, 1
        for i in range(n - 1):
            b, a = a + b, b
        return b

    @staticmethod
    def fib_dp(n: int):
        """用 DP 数组存储每一步计算的结果，避免重复计算"""
        dp = [0] * (n + 1)

        dp[0], dp[1] = 0, 1

        if n in [0, 1]:
            return n

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    def test_fib(self):
        res = self.fib(33)
        logger.info(f"Fibonacci：{res}")

    def test_fib_note(self):
        res = self.fib_note(33)
        logger.info(f"Note Fibonacci：{res}")

    def test_fib_dp(self):
        res = self.fib_dp(33)
        logger.info(f"DP Array Fibonacci：{res}")

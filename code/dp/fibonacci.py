import unittest
from code import logger


class Fibonacci(unittest.TestCase):
    def fib(self, n: int):
        if n in [0, 1]:
            return n
        return self.fib(n - 1) + self.fib(n - 2)  # 调了两次递归，造成重复的计算，可以用动态规划思想优化

    def test_fib(self):
        res = self.fib(33)
        logger.info(f"Fibonacci：{res}")

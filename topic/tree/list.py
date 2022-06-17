import unittest
from topic import logger


class ListCase(unittest.TestCase):
    """列表打印"""

    def traverse(self, data: list, index: int = 0):
        """倒序打印列表"""
        if index >= len(data):
            return
        self.traverse(data, index + 1)
        logger.info(data[index])

    def test(self):
        data = [1, 2, 3, 4, 5]
        self.traverse(data)

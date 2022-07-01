import unittest
from topic import logger


class Backtrack(unittest.TestCase):
    """回溯算法"""

    def __init__(self, *args, **kwargs):
        super(Backtrack, self).__init__(*args, **kwargs)

    def permutation(self, numbers: list, record: list):
        """排列组合"""

        # 一个完整的排列
        if len(record) == len(numbers):
            logger.info(record)
            return

        for number in numbers:
            if number in record:
                continue

            # 选中 number
            record.append(number)

            # 选择下一个
            self.permutation(numbers, record)

            # 移除 number
            record.remove(number)

    def test_permutation(self):
        numbers = [1, 2, 3]
        self.permutation(numbers, [])


if __name__ == "__main__":
    unittest.main()

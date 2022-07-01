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

    def n_queen(self, n):
        """N 皇后问题"""

        queen_board = [[0 for _ in range(n)] for _ in range(n)]

        def is_valid(board, row, col):
            """检查是否可以放在当前格子
            只需要检查上方，左上方，右上方是否有就行
            因为下棋方向是从上往下，下方不会有棋子，而且每一行只有一个棋子
            """

            # 上方检查
            for i in range(row):
                if board[i][col] == 1:
                    return False

            # 左上方检查
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 1:
                    return False
                i -= 1
                j -= 1

            # 右上方检查
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 1:
                    return False
                i -= 1
                j += 1

            return True

        def traceback(board, row):
            """棋盘中所有位置的全排列"""
            if row >= len(board):
                logger.info(board)
                return board

            col_no = len(board[row])

            for col in range(col_no):
                if not is_valid(board, row, col):
                    continue

                # 放入棋盘
                board[row][col] = 1

                # 检查下一行
                traceback(board, row + 1)

                # 拿回来，以便于检查下一列
                board[row][col] = 0

        traceback(queen_board, 0)

    def test_permutation(self):
        numbers = [1, 2, 3]
        self.permutation(numbers, [])

    def test_n_queen(self):
        self.n_queen(4)


if __name__ == "__main__":
    unittest.main()

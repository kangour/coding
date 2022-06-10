import unittest
from code import logger


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeCase(unittest.TestCase):
    def traverse(self, root: TreeNode):
        """二叉树前序遍历"""
        if not root:
            return
        logger.info(root.value)
        self.traverse(root.left)
        self.traverse(root.right)

    def test(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.traverse(root)


class ListCase(unittest.TestCase):
    def traverse(self, data: list, index: int = 0):
        """倒序打印列表"""
        if index >= len(data):
            return
        self.traverse(data, index + 1)
        logger.info(data[index])

    def test(self):
        data = [1, 2, 3, 4, 5]
        self.traverse(data)

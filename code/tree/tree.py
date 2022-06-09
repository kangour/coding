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

import unittest
from code import logger


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TreeCase(unittest.TestCase):
    """二叉树打印"""

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


class TreeDepthCase(unittest.TestCase):
    """二叉树深度"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.depth = 0
        self.res = 0

    def traverse_depth_preorder(self, root: TreeNode):
        """先序遍历，计算二叉树最大深度
        进入递归 +1，退出 -1。没有子节点时，统计一个最大深度"""

        if not root:
            return

        self.depth += 1

        # 这个 res 的判断，放在 depth++ 与 depth-- 之间的任何位置都行
        # 它对前中后序的位置不敏感，习惯性放前序位置
        if root.left is None and root.right is None:
            self.res = max(self.res, self.depth)

        self.traverse_depth_preorder(root.left)
        self.traverse_depth_preorder(root.right)

        self.depth -= 1

        return self.res

    def test_depth(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)

        res = self.traverse_depth_preorder(root)
        logger.info(res)


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


class LinkCase(unittest.TestCase):
    """链表打印"""

    def traverse(self, head: LinkNode):
        """倒序打印链表"""
        if not head:
            return
        self.traverse(head.next)
        logger.info(head.value)

    def test(self):
        head = LinkNode(1)
        head.next = LinkNode(2)
        head.next.next = LinkNode(3)
        self.traverse(head)

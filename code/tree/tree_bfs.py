import unittest
from code import logger
from code.tree.schema import TreeNode


class TreeBFSCase(unittest.TestCase):
    """递归遍历，二叉树广度优先"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bfs_nodes = []

    def traverse(self, nodes: list):
        if not nodes:
            return

        sub_nodes = []

        for node in nodes:
            if not node:
                continue
            self.bfs_nodes.append(node.value)

            sub_nodes.append(node.left)
            sub_nodes.append(node.right)

        self.traverse(sub_nodes)

        return self.bfs_nodes

    @staticmethod
    def traverse_while(root):
        """循环遍历，二叉树广度优先"""

        if not root:
            return

        nodes = [root]
        bfs_nodes = []

        while nodes:
            _nodes = []
            for node in nodes:
                if not node:
                    continue
                bfs_nodes.append(node.value)

                _nodes.append(node.left)
                _nodes.append(node.right)
            nodes = _nodes

        return bfs_nodes

    def test_depth(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        data = [root]

        res = self.traverse(data)
        logger.info(f"BFS：递归分层遍历二叉树：{res}")

        res = self.traverse_while(root)
        logger.info(f"BFS：循环分层遍历二叉树：{res}")

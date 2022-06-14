import unittest
from code import logger
from code.tree.schema import LinkNode


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

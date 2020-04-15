# 在O(1)时间内删除链表结点

'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''


class ListNode:

    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution:

    def deletenode(self, head, target):
        if not head or not target:
            return None
        elif target.next == None:
            while head.next != target:
                head = head.next
            head.next = None
            target.__del__()
        elif target.next != None:
            target.val == target.next.val
            target.next == target.next.next
            target.__del__()

s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s.deletenode(node1, node3)
print(node3.next)



# 反转链表

'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

# 迭代实现反转链表


class Solution:

    def ReverseList(self, pHead):
        pNode = pHead
        pNext = None
        pPrev = None
        while pNode != None:
            pNext = pNode.next
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pPrev


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3
singlenode = ListNode(1)
s = Solution()
p = s.ReverseList(singlenode)
print(p.next.val)
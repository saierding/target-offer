# 两个链表的第一个公共结点

'''
输入两个链表，找出它们的第一个公共结点。
'''


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 比较两个链表长短，让长的和短的同时走，直到遇到相同的停
    def FindFirstCommonNode(self, pHead1, pHead2):
        pHead1_len = self.listnode_length(pHead1)
        pHead2_len = self.listnode_length(pHead2)
        len_diff = abs(pHead1_len-pHead2_len)

        if pHead1_len > pHead2_len:
            pHead_long = pHead1
            pHead_short = pHead2
        else:
            pHead_long = pHead2
            pHead_short = pHead1

        while len_diff > 0:
            pHead_long = pHead_long.next
            len_diff -= 1

        while pHead_long != None and pHead_short != None and pHead_long.val != pHead_short.val:
            pHead_long = pHead_long.next
            pHead_short = pHead_short.next

        return pHead_long

    def listnode_length(self, pHead):
        length = 0
        while pHead != None:
            pHead = pHead.next
            length += 1
        return length


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node4.next = node5
node5.next = node6

s = Solution()
print(s.FindFirstCommonNode(node1, node4))
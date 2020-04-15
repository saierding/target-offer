# 合并两个排序的链表

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def Merge(self, pHead1, pHead2):
        pMerge = None
        if pHead1 == None and pHead2 == None:
            return None
        elif pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        else:
            if pHead1.val < pHead2.val:
                pMerge = pHead1
                pMerge.next = self.Merge(pHead1.next, pHead2)
            else:
                pMerge = pHead2
                pMerge.next = self.Merge(pHead1, pHead2.next)
        return pMerge


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()
S.Merge(node1, node4)
print(node2.next.val)
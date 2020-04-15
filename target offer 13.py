# 链表中倒数第k个结点

'''
输入一个链表，输出该链表中倒数第k个结点。
'''


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindKthToTail(self, head, k):
        length = 1
        if head == None or k <= 0:
            return None
        dummy = head
        while dummy.next != None:
            dummy = dummy.next
            length += 1
        if k > length:
            return None
        else:
            for i in range(length-k):
                head = head.next
            return head


'''
这道题的思路很好
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''


# class Solution:
#
#     def FindKthToTail(self, head, k):
#         if head == None or k <= 0:
#             return None
#
#         pAHead = head
#         pBehind = None
#
#         for i in range(k - 1):
#             if pAHead.next != None:
#                 pAHead = pAHead.next
#             else:
#                 return None
#         pBehind = head
#         while pAHead.next != None:
#             pAHead = pAHead.next
#             pBehind = pBehind.next
#         return pBehind


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
print(s.FindKthToTail(node1, 5).val)


# 从头到尾打印链表

'''
输入一个链表，从尾到头打印链表每个节点的值。
'''


class ListNode:

    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:

    def print_listnode(self, listnode):
        output_list = []

        while listnode:
            output_list.append(listnode.val)
            listnode = listnode.next
        output_list.reverse()
        return output_list


node1 = ListNode(1)
node2 = ListNode(5)
node3 = ListNode(99)
node1.next = node2
node2.next = node3
s = Solution()

print(s.print_listnode(node1))


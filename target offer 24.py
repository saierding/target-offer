# 复杂链表的复制

'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
'''


class RandomListNode:

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CreateNewNode(pHead)
        self.CreateNewRandom(pHead)
        return self.ReconnectNode(pHead)

    # 创建新的一样的节点，并把新节点连接到以前的节点的后面
    def CreateNewNode(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next

    # 将新的节点的random指针指向对应的节点上去
    def CreateNewRandom(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 将新生成的分成两半按奇偶，即成功复制
    def ReconnectNode(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedHead.next
        pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)











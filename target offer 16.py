# 树的子结构

'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def tree1hastree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        elif pRoot1 == None:
            return False
        elif pRoot1.val != pRoot2.val:
            return False
        return self.tree1hastree2(pRoot1.left, pRoot2.left) and self.tree1hastree2(pRoot1.right, pRoot2.right)

    def hassubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.tree1hastree2(pRoot1, pRoot2)
            if not result:
                result = self.hassubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.hassubtree(pRoot1.right, pRoot2)
        return result


pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

s = Solution()
print(s.hassubtree(pRoot1, pRoot8))
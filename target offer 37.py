# 二叉树的深度

'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 笨办法，递归求出所有路径，然后求最大
    # def TreeDepth1(self, pRoot):
    #     if not pRoot:
    #         return []
    #     elif pRoot.left == None and pRoot.right == None:
    #         return [[pRoot.val]]
    #     stack = []
    #     leftstack = self.TreeDepth(pRoot.left)
    #     for i in leftstack:
    #         i.insert(0, pRoot.val)
    #         stack.append(i)
    #     rightstack = self.TreeDepth(pRoot.right)
    #     for i in rightstack:
    #         i.insert(0, pRoot.val)
    #         stack.append(i)
    #     return stack
    #
    # def TreeDepth(self, pRoot):
    #     stack = self.TreeDepth(pRoot)
    #     stack_len = []
    #     for i in stack:
    #         stack_len.append(len(i))
    #     return max(stack_len)


    # 利用递归，比较左右子树大小+1即可
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))+1


pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

s = Solution()
print(s.TreeDepth(pNode1))



# 二叉树中和为某一值的路径

'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def FindPath(self, root, sum):
        if not root:
            return []
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        stack = []
        leftstack = self.FindPath(root.left, sum-root.val)
        for i in leftstack:
            i.insert(0, root.val)
            stack.append(i)
        rightstack = self.FindPath(root.right, sum-root.val)
        for i in rightstack:
            i.insert(0, root.val)
            stack.append(i)
        return stack


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution()
print(S.FindPath(pNode1, 22))



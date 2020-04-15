# 二叉树的最低公共祖先


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 二叉搜索树直接递归
    # def lowestCommonAncestor(self, root, A, B):
    #     if root == None:
    #         return False
    #     if root.val > A.val and root.val > B.val:
    #         return self.lowestCommonAncestor(root.left, A, B)
    #     elif root.val < A.val and root.val < B.val:
    #         return self.lowestCommonAncestor(root.right, A, B)
    #     return root.val

    # 二叉搜索树迭代
    def lowestCommonAncestor(self, root, A, B):
        if root == None:
            return False
        while root:
            if root.val > A.val and root.val > B.val:
                root = root.left
            elif root.val < A.val and root.val < B.val:
                root = root.right
            else:
                return root.val


node0 = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node6.left = node2
node6.right = node8
node2.left = node0
node2.right = node4
node8.left = node7
node8.right = node9
node4.left = node3
node4.right = node5
s = Solution()
print(s.lowestCommonAncestor(node6, node0, node5))

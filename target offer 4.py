# 重建二叉树

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def reconstruct(self, pre, mid):
        if not pre and not mid:
            return None
        if set(pre) != set(mid):
            return None
        root = TreeNode(pre[0])
        i = mid.index(pre[0])
        root.left = self.reconstruct(pre[1:i+1], mid[0:i])
        root.right = self.reconstruct(pre[i+1:-1], mid[i+1:-1])
        return root


pre_input = [1, 2, 4, 7, 3, 5, 6, 8]
mid_input = [4, 7, 2, 1, 5, 3, 8, 6]
s = Solution()
print(s.reconstruct(pre_input, mid_input))


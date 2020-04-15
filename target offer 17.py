# 二叉树的镜像

'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归实现
# class Solution:
#
#     def Mirror(self, root):
#         if root == None:
#             return None
#         if root.left == None and root.right == None:
#             return root
#
#         ptemp = root.left
#         root.left = root.right
#         root.right = ptemp
#
#         self.Mirror(root.left)
#         self.Mirror(root.right)


# 非递归实现
class Solution:

    def Mirror(self, root):
        if root == None:
            return None
        curnode = []
        curnode.append(root)
        while len(curnode) > 0:
            number = len(curnode)-1
            tree = curnode[number]
            curnode.pop()
            if tree.left != None or tree.right != None:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:
                curnode.append(tree.left)
            if tree.right:
                curnode.append(tree.right)


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = Solution()
s.Mirror(pNode1)
print(pNode1.left.val)
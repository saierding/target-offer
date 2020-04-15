# 二叉树的后序遍历

'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''


class Solution:

    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        length = len(sequence)
        cur_root = sequence[-1]
        if min(sequence) > cur_root or max(sequence) < cur_root:
            return True

        index = 0
        for i in range(length-1):
            index = i
            if sequence[i] > cur_root:
                break

        for j in range(index+1, length-1):
            if sequence[j] < cur_root:
                return False

        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])

        right = True
        if index < length-1:
            right = self.VerifySquenceOfBST(sequence[index:length-1])

        return left and right


array2 = [4, 6, 7, 5]
S = Solution()
print(S.VerifySquenceOfBST(array2))

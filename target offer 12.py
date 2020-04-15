# 调整数组顺序使奇数位于偶数前面

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


class Solution:

    def reorderarray(self, array):
        left = []
        right = []
        for x in array:
            if x & 1:
                left.append(x)
            elif not x & 1:
                right.append(x)
        return left + right


s = Solution()
print(s.reorderarray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))


# 打印1到最大的n个数

'''
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
'''


class Solution:

    def print_maxnumber(self, n):
        i = 0
        count = 1
        while i < n:
            count *= 10
            i += 1
        for i in range(count):
            pass
        return i


s = Solution()
print(s.print_maxnumber(8))

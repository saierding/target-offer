# 约瑟夫环

'''
0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
求这个圆圈中最后剩下的一个数字
'''


class Solution:

    # 数学建模(原理并没有看懂)
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        remainIndex = 0
        for i in range(1, n+1):
            remainIndex = (remainIndex + m) % i
        return remainIndex


s = Solution()
print(s.LastRemaining_Solution(5, 3))
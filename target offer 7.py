# 斐波那契数列

'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

# 笨办法--递归（有太多重复项了）
# class Solution:
#
#     def fib(self, n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n-2) + self.fib(n-1)
#
#
# s = Solution()
# print(s.fib(13))

# 好方法（使用循环解决，从下到上这样可以避免很多重复项计算）


class Solution:

    def fib(self, n):
        fib_front = 0
        fib_rear = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        for i in range(2, n+1):
            ans = fib_front + fib_rear
            fib_front = fib_rear
            fib_rear = ans
        return ans


s = Solution()
print(s.fib(6000))
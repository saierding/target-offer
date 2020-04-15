# 数值的整数次方
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
'''

'''
需要注意的地方:
当指数为负数的时候
当底数为零切指数为负数的情况
在判断底数base是不是等于0的时候,不能直接写base==0, 因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内
'''


class Solution:

    def power(self, base, exponent):
        result = 1
        if exponent == 0:
            return 1
        elif exponent < 0:
            if base == 0:
                return 0
            else:
                for i in range(-exponent):
                    result *= base
                    ans = 1/result
                return ans
        elif exponent > 0:
            if base == 0:
                return 0
            else:
                for i in range(exponent):
                    result *= base
                    ans = result
                return ans


s = Solution()
print(s.power(2, -3))









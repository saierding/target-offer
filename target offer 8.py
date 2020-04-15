# 二进制中1的个数

'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

# 使用python自带的bin方法转化成二进制然后进行计算


class Solution:

    def numberofone(self, n):
        count = 0
        if n >= 0:
            ans = bin(n).replace('0b', '')
            for i in ans:
                if i == '1':
                    count += 1
            return count
        elif n < 0:
            ans = bin(n & 0xffffffff)
            for i in ans:
                if i == '1':
                    count += 1
            return count


# s = Solution()
# print(s.numberofone(10))








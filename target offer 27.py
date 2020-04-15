# 数组中超过一半的数字

'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''


class Solution:

    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        numbers.sort()
        lenNum = len(numbers)
        mid = lenNum//2
        count = numbers.count(numbers[mid])
        if count > lenNum/2:
            return numbers[mid]
        else:
            return 0


S = Solution()
print(S.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.MoreThanHalfNum_Solution([1, 2, 3, 3, 3, 3, 4]))
print(S.MoreThanHalfNum_Solution([1, 2]))

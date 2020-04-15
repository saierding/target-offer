# 数组中重复的数字

'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''


class Solution:
    # 用字典保存并求解
    def duplicate2(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers) - 1:
                return False
        repeatedNums = []
        dict = {}
        for i in range(len(numbers)):
            if numbers[i] not in dict.keys():
                dict[numbers[i]] = 0
            dict[numbers[i]] += 1
        for i in dict:
            if dict[i] != 1:
                repeatedNums.append(i)
        return repeatedNums

    #
    # def duplicate2(self, numbers):
    #     if numbers == None or len(numbers) <= 0:
    #         return False
    #     for i in numbers:
    #         if i < 0 or i > len(numbers) - 1:
    #             return False
    #     repeatedNums = []
    #     for i in range(len(numbers)):
    #         while numbers[i] != i:
    #             if numbers[i] == numbers[numbers[i]]:
    #                 repeatedNums.append(numbers[i])
    #                 break
    #             else:
    #                 index = numbers[i]
    #                 numbers[i], numbers[index] = numbers[index], numbers[i]
    #     return repeatedNums


test = [2, 3, 1, 0, 2, 5, 3]
s = Solution()
print(s.duplicate2(test))

# 连续子数组的最大和

'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''


class Solution:

    # fixed windows size

    # def FindGreatestSumOfSubArray(self, array):
    #     arr_len = len(array)
    #     max_num = -float('inf')
    #     if array == None or arr_len <= 0:
    #         return 0
    #     else:
    #         for win_len in range(1, arr_len+1):
    #             for i in range(0, arr_len+1-win_len):
    #                 cur_sum = sum(array[i:i+win_len])
    #                 max_num = max(cur_sum, max_num)
    #         return max_num



    # fixed start index

    # def FindGreatestSumOfSubArray(self, array):
    #     arr_len = len(array)
    #     max_num = -float('inf')
    #     if array == None or arr_len <= 0:
    #         return 0
    #     else:
    #         for start in range(0, arr_len):
    #             for win_len in range(1, arr_len+1-start):
    #                 cur_sum = sum(array[start:start+win_len])
    #                 max_num = max(cur_sum, max_num)
    #         return max_num


    # dp algorithm

    def FindGreatestSumOfSubArray(self, array):
        arr_len = len(array)
        max_num = -float('inf')
        max_sofar = 0
        if array == None or arr_len <= 0:
            return 0
        else:
            for i in array:
                max_sofar = max(max_sofar+i, i)
                max_num = max(max_num, max_sofar)
            return max_num


alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.FindGreatestSumOfSubArray(alist))
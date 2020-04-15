# 和为s的两个数字

'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''


class Solution:

    # 方法一
    # def FindNumbersWithSum(self, array, tsum):
    #     if array == None or len(array) <= 0 or tsum < array[0]:
    #         return []
    #     else:
    #         new_list = []
    #         for i in array:
    #             index = tsum - i
    #             if index in array and index not in new_list:
    #                 new_list.append(i)
    #             else:
    #                 continue
    #         if new_list == None or len(new_list) == 0:
    #             return []
    #         else:
    #             answer = new_list[0]
    #             return [answer, tsum-answer]

    # 方法二
    # 从左右一起查找,因为当两个数的和一定的时候, 两个数字的间隔越大, 乘积越小
    # 所以直接输出查找到的第一对数即可
    def FindNumbersWithSum(self, array, tsum):
        if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []
        else:
            start = 0
            end = len(array)-1
            while start < end:
                sum = array[start] + array[end]
                if sum < tsum:
                    start += 1
                elif sum > tsum:
                    end -= 1
                else:
                    return [array[start], array[end]]
            return []

test = [1,2,4,7,11,16]
s = Solution()
print(s.FindNumbersWithSum(test, 10))
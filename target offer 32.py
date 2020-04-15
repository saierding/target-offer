# 丑数

'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''


class Solution:

    # 笨办法，先写一个判断是否是丑数的函数,再循环遍历所有数进行判断

    # def isUgly(self, number):
    #     if number <= 0 or number == None:
    #         return False
    #     else:
    #         while number % 2 == 0:
    #             number /= 2
    #         while number % 3 == 0:
    #             number /= 3
    #         while number % 5 == 0:
    #             number /= 5
    #         if number == 1:
    #             return True
    #         else:
    #             return False
    #
    # def GetUglyNumber_Solution(self, index):
    #     if index <= 0 or index == None:
    #         return 0
    #     else:
    #         ugly_count = 0
    #         number = 0
    #         while ugly_count < index:
    #             number += 1
    #             if self.isUgly(number):
    #                 ugly_count += 1
    #         return number

    # 利用空间换时间的办法，建立一个index长度的数组来存排序好的丑数
    def GetUglyNumber_Solution(self, index):
        if index == None or index <= 0:
            return 0
        else:
            ugly_list = [1]*index
            index_list = 1
            index2, index3, index5 = 0, 0, 0
            while index_list < index:
                min_val = min(ugly_list[index2]*2, ugly_list[index3]*3, ugly_list[index5]*5)
                ugly_list[index_list] = min_val
                while ugly_list[index2]*2 <= ugly_list[index_list]:
                    index2 += 1
                while ugly_list[index3]*3 <= ugly_list[index_list]:
                    index3 += 1
                while ugly_list[index5]*5 <= ugly_list[index_list]:
                    index5 += 1
                index_list += 1
            return ugly_list[-1]


s = Solution()
print(s.GetUglyNumber_Solution(1))
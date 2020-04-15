# 数字在排序数组中出现的次数

'''
统计一个数字在排序数组中出现的次数。
'''


class Solution:

    def GetNumberOfK(self, data, k):
        if data == None or len(data) < 0 or k not in data:
            return -1
        else:
            copy_dict = {}
            for i in data:
                if i not in copy_dict.keys():
                    copy_dict[i] = 0
                copy_dict[i] += 1
            return copy_dict[k]


alist = [3, 3, 3, 3, 4, 5]
s = Solution()
print(s.GetNumberOfK(alist, 3))
# 数组中只出现一次的数字

'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''


class Solution:

    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None or len(array) <= 0:
            return []
        else:
            array_dict = {}
            for i in array:
                if i not in array_dict.keys():
                    array_dict[i] = 0
                array_dict[i] += 1
            array_list = []
            for i in array_dict:
                if array_dict[i] == 1:
                    array_list.append(i)
            return array_list


aList = [2, 4, 3, 6, 3, 2, 5, 5]
s = Solution()
print(s.FindNumsAppearOnce(aList))
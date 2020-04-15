# 数组中的逆序对

'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
'''


class Solution:

    # 笨办法，直接用冒泡排序

    # def InversePairs(self, data):
    #     if len(data) <= 0:
    #         return 0
    #     else:
    #         count = 0
    #         for i in range(0, len(data)-1):
    #             for j in range(i+1, len(data)):
    #                 if data[i] > data[j]:
    #                     count += 1
    #         return count

    # 用数字规律做,利用index求解
    def InversePairs(self, data):
        if len(data) <= 0:
            return 0
        else:
            count = 0
            copy = []
            for i in data:
                copy.append(i)
            copy.sort()
            i = 0
            while i < len(copy):
                copy_index = data.index(copy[i])
                count += copy_index
                data.remove(copy[i])
                i += 1
            return count


s = Solution()
print(s.InversePairs(
    [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460,
     505, 360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550,
     474, 162, 268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583,
     523, 697, 478, 147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425,
     930, 64, 266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]))
print(s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))

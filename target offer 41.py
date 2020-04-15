# 和为s的连续整数序列

'''
找出所有和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''


class Solution:

    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small, big = 1, 2
        curSum = small+big
        middle = (tsum+1)//2
        output_list = []
        while small < middle:
            if curSum == tsum:
                output_list.append(list(range(small, big + 1)))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output_list


s = Solution()
print(s.FindContinuousSequence(15))

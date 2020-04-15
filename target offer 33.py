# 第一个只出现一次的字符

'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''


class Solution:

    def FirstNotRepeatingChar(self, s):
        if s == None or len(s) <= 0:
            return -1
        else:
            output_list = {}
            input_list = list(s)
            for i in range(len(input_list)):
                if input_list[i] not in output_list.keys():
                    output_list[input_list[i]] = 0
                output_list[input_list[i]] += 1
            for i in range(len(input_list)):
                if output_list[input_list[i]] == 1:
                    return i
            return -1


s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))
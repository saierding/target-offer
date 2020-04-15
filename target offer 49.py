# 把字符串转换成整数

'''
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数
'''


class Solution:

    # 利用库函数
    def StrToInt(self, s):
        if s == None or len(s) <= 0:
            return 0
        if s == '0':
            return 0
        output = []
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s:
            if i in dict.keys():
                output.append(dict[i])
            elif i == '+':
                continue
            elif i == '-':
                continue
            else:
                return 0
        ans = 0
        for i in output:
            ans = ans * 10 + i
        if s[0] == '-':
            ans = -ans
        return ans


test = '-12356'
s = Solution()
print(s.StrToInt(test))
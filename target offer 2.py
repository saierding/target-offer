# 替换字符串

'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''


class Solution:

    def stringReplace(self, s):
        init_string = ''
        if type(s) != str:
            return False
        for i in s:
            if i == ' ':
                init_string += '%20'
            else:
                init_string += i
        return init_string


answer = Solution()
print(answer.stringReplace('we are happy'))

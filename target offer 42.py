# 翻转单词顺序

'''
输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
为简单起见, 标点符号和普通字母一样处理
'''


class Solution:

    # python 反转字符串的方法
    def ReverseSentence(self, s):
        l = s.split(' ')
        return ' '.join(l[::-1])


str = 'I am a student.'
s = Solution()
print(s.ReverseSentence(str))
# 字符串的左旋转

'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
'''


class Solution:

    def LeftRotateString(self, s, n):
        if len(s) <= 0 or len(s) < n or n < 0:
            return ''
        str_list = list(s)
        output_list1 = str_list[n:]
        output_list2 = str_list[:n]
        return ''.join(output_list1)+''.join(output_list2)


test = 'abcdefg'
s = Solution()
print(s.LeftRotateString(test, 2))
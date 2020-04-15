# 包含min函数的栈

'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''


class Solution:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def min(self):
        return self.minstack[-1]

    def push(self, node):
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            temp = self.min()
            self.minstack.append(temp)

    def pop(self):
        if self.stack == [] or self.minstack == []:
            return None
        else:
            self.minstack.pop()
            self.stack.pop()


s = Solution()
s.push(3)
s.push(4)
s.push(2)
s.push(1)
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())
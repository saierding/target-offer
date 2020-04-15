# 构建乘积数组

'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''


class Solution:

    def multiply(self, A):
        if A == None or len(A) <= 0:
            return
        B_list = [1]*len(A)
        # 从上到下先把A[i-1]以前的都乘️进去
        for i in range(1, len(A)):
            B_list[i] = A[i-1] * B_list[i-1]
        # 从下到上再把A[i+1]以后的都乘进去
        temp = 1
        for i in range(len(A)-2, -1, -1):
            temp = temp * A[i+1]
            B_list[i] = B_list[i] * temp
        return B_list


test = [1, 2, 3, 4]
s = Solution()
print(s.multiply(test))
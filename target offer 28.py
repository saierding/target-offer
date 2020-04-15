# 最小的k个数

'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''


class Solution:

# 直接用sort函数作弊

    # def GetLeastNumbers_Solution(self, tinput, k):
    #     tinput.sort()
    #     if k > len(tinput):
    #         return []
    #     elif k < 1:
    #         return []
    #     else:
    #         output_list = tinput[0:k]
    #         return output_list

# O(nlogk)的算法, 适合海量数据
# 利用一个k容量的容器存放数组, 构造最大堆, 当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数

    def GetLeastNumbers_Solution(self, tinput, k):
        import heapq
        output = []
        if k > len(tinput):
            return []
        elif k < 1:
            return []
        else:
            for i in tinput:
                if len(output) < k:
                    output.append(i)
                    output = heapq.nlargest(len(output), output)
                else:
                    output = heapq.nlargest(k, output)
                    if i > output[0]:
                        continue
                    else:
                        output[0] = i
            return output[::-1]


tinput = [4,5,1,6,2,7,3,8]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput, 8))
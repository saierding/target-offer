# 寻找二维数组的target

'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
查找方式从右上角开始查找
如果当前元素大于target, 左移一位继续查找
如果当前元素小于target, 下移一位继续查找
进行了简单的修改, 可以判定输入类型为字符的情况
array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
'''


class Solution:

    def find(self, array, target):
        row = len(array)
        column = len(array[0])
        i, j = 0, column-1
        while i <= row-1 and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i += 1
            elif array[i][j] > target:
                j -= 1
        return False

    def locate(self, array, target):
        row = len(array)
        column = len(array[0])
        count = 0
        i, j = 0, column-1
        while i <= row-1 and j >= 0:
            if array[i][j] == target:
                count += 1
                j -= 1
            elif array[i][j] < target:
                i += 1
            elif array[i][j] > target:
                j -= 1
        return count


array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
answer = Solution()
print(answer.find(array, 90))
print(answer.locate(array, 9))



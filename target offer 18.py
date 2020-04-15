# 顺时针打印矩阵

'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''


class Solution:

    def printmatrix(self, matrix):
        output_list = []
        start = 0
        row = len(matrix)
        col = len(matrix[0])
        if matrix == None:
            return None
        if matrix == []:
            return []
        while start*2 < row and start*2 < col:
            endx = col - 1 - start
            endy = row - 1 - start
            # 从左往右遍历
            for i in range(start, endx+1):
                number = matrix[start][i]
                output_list.append(number)
            # 从上到下遍历，需要判断是否只有一行
            if start < endy:
                for i in range(start+1, endy+1):
                    number = matrix[i][endx]
                    output_list.append(number)
            # 从右到左遍历，需要判断是否只有一行并且是否只有一列
            if start < endy and start < endx:
                for i in range(endx-1, start-1, -1):
                    number = matrix[endy][i]
                    output_list.append(number)
            # 从下往上遍历，需要判断是否只有一行并且只有一列
            if start < endy-1 and start < endx:
                for i in range(endy-1, start, -1):
                    number = matrix[i][start]
                    output_list.append(number)
            start += 1
        return output_list


matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1], [2], [3], [4], [5]]
matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

s = Solution()
print(s.printmatrix(matrix3))
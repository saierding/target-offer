# 旋转数组中的最小数字

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


class Solution:

    def findminnunmber(self, input_list):
        index0 = 0
        index1 = len(input_list)-1
        ans = input_list[0]
        if len(input_list) == 0:
            return 0
        elif input_list[index0] < input_list[index1]:
            return input_list[0]
        else:
            while index1-index0 > 1:
                mid = index0 + (index1-index0)//2
                if input_list[mid] > input_list[index0]:
                    index0 = mid
                elif input_list[mid] < input_list[index1]:
                    index1 = mid
                elif input_list[index0] == input_list[index1] and input_list[mid] == input_list[index0]:
                    for i in range(1, len(input_list)):
                        if input_list[i] < ans:
                            ans = input_list[i]
                            return ans
            return input_list[index1]


s = Solution()
test_input = [3, 5, 7, 8, 10, 2]
print(s.findminnunmber(test_input))









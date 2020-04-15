# n个骰子的点数

'''
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
'''


class Solution:
    # 动态规划
    # 构造两个数组来存储骰子点数的每一个总数出现的次数
    # 在一次循环中, 第一个数组中的第n个数字表示骰子和为n出现的次数
    # 在下次循环中, 另一个数组的第n个数字设为前一个数组对应的第n-1、n-2、n-3、n-4、n-5、n-6之和
    def PrintProbability(self, number):
        if number < 1:
            return []
        max_val = 6
        storage = [[], []]
        storage[0] = [0] * (max_val * number + 1)
        flag = 0
        for i in range(1, max_val+1):
            storage[flag][i] = 1
        for i in range(2, number+1):
            storage[1-flag] = [0] * (max_val * number + 1)
            for j in range(i, i*max_val+1):
                dice_num = 1
                while dice_num < j and dice_num < max_val:
                    storage[1-flag][j] += storage[flag][j-dice_num]
                    dice_num += 1
            flag = 1 - flag
        total = max_val ** number
        for i in range(number, number*max_val+1):
            percent = storage[flag][i] / float(total)
            print("{}: {:e}".format(i, percent))


s = Solution().PrintProbability(5)





# 整数中1出现的次数

'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''


class Solution:

    # 笨办法，每一位判断一次，一次%10查1
    # def NumberOf1Between1AndN_Solution(self, n):
    #     count = 0
    #     for i in range(0, n+1):
    #         temp = i
    #         while temp:
    #             if temp % 10 == 1:
    #                 count += 1
    #             temp = temp//10
    #     return count

    # 利用数字规律的办法
    '''
    https://github.com/WordZzzz/Note/blob/master/AtOffer/《剑指offer》刷题笔记（时间效率）：整数中1出现的次数（从1到n整数中1出现的次数）.md
    '''  
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        i = 1
        while i <= n:
            a = n // i
            b = n % i
            index_i = a - n // (i*10) * 10
            if index_i == 0:
                count += ((a // 10) * i)
            elif index_i == 1:
                count += ((a // 10) * i + (b + 1))
            else:
                count += (((a // 10) + 1) * i)
            i *= 10
        return count


s = Solution()
print(s.NumberOf1Between1AndN_Solution(13))
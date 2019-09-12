# -*- coding:utf-8 -*-
class Solution:
    def jumpSteps1(self, n): # write code here
        # 递归的方式，时间复杂度为2^n
        if n == 0:
            return "none"
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.jumpSteps1(n - 2) + self.jumpSteps1(n - 1)

    def jumpSteps2(self, n):
        # 循环的方式，时间复杂度为n
        if n == 0:
            return "none"
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        a = 2
        b = 1
        ret = 0

        for i in range(0, n - 2):
            ret = a + b
            b = a
            a = ret

        return ret

if __name__ == '__main__':
    s = Solution()
    s.jumpSteps1(n) # n需要替换成任意一个数字
    s.jumpSteps2(n) # n需要替换成任意一个数字

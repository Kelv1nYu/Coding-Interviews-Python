# -*- coding:utf-8 -*-
class Solution:
    def jumpSteps1(self, n): # write code here
        # 递归的方式
        if n == 0:
            return "none"
        elif n == 1:
            return 1

        else:
            return self.jumpSteps1(n - 1) *2

    def jumpSteps2(self, n):
        # 循环的方式
        if n == 0:
            return "none"
        elif n == 1:
            return 1

        a = 1
        ret = 0

        for i in range(0, n - 1):
            ret = a * 2
            a = ret

        return ret

    def jumpSteps3(self, n):
        # 找规律方法，直接使用内置函数
        return pow(2, n -1)


if __name__ == '__main__':
    s = Solution()
    print(s.jumpSteps1(n))
    print(s.jumpSteps2(n))
    print(s.jumpSteps3(n))

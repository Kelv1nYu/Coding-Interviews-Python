# 递归的方式，时间复杂度为2^n
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            return self.Fibonacci(n - 2) + self.Fibonacci(n-1)
          
if __name__ == '__main__':
    s = Solution()
    n = input()
    s.Fibonacci(n)

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci1(self, n):
        # write code here
        # 递归的方式，时间复杂度为2^n
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            return self.Fibonacci(n - 2) + self.Fibonacci(n-1)
        
    def Fibonacci2(self, n):
        # 循环的方式
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a = 1
        b = 0
        
        for i in range(0, n - 1):
            ret = a + b
            b = a
            a = ret
            
        return ret
          
if __name__ == '__main__':
    s = Solution()
    n = input()
    s.Fibonacci(n)

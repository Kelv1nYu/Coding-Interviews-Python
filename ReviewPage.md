# Review Page

本页面为所有代码的做法与总结。

---
**0. [Fibonacci](https://github.com/Kelv1nYu/)**      Level: Easy

斐波那契数列:

递归的思想：
      
      n = 0, num = 0
      
      n = 1, num = 1
      
      n = 2, num = 1
      
      ...
      
      n = k(k > 1), f(k) = (k-1) + (k-2)
      
      n = 0, f(0) = 0
      
      n = 1, f(1) = 1
      
循环的思想：

      n = 0, num = 0
      n = 1, num = 1
      n = 2, num = 0 + 1
      
      a = 1   # a存放较大的数
      b = 0   # b存放较小的数
      ret = 0 # ret用来暂存 a + b 的和
      
      # 开始循环，循环体内：
      ret = a + b
      b = a   # 将a的值赋给b，作为下一次计算的b
      a = ret # 将ret（a + b）的值赋给a，作为下一次计算的a

---

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find1(self, target, array):
        # 循环嵌套的方式，时间复杂度为n^2
        for i in range(len(array)):
            for j in range(len(array[i])):
                if target == array[i][j]:
                    return True

        return False

    def Find2(self, target, array):

        # 拟指针移动方式，时间复杂度为n
        row_count = len(array)
        col_count = len(array[0])
        i = 0
        j = col_count - 1

        while i < row_count and j >= 0:
            value = array[i][j]
            if target == value:
                return True
            elif target < value:
                j -= 1
            else:
                i += 1

        return False

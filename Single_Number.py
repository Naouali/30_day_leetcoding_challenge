#!/usr/bin/python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dic = {}
        value = 0
        for i in nums:
            my_dic[i] = 0
        for i in nums:
            my_dic[i] += 1
        for x in my_dic:
            if my_dic[x] == 1:
                value = x
        return value

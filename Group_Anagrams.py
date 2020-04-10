#!/usr/bin/python3
#Given an array of strings, group anagrams together.

#Example:

#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]

def anagram(a):
    my_dic = {}
    my_list = []
    words = []
    for i in a:
        my_dic[i] = _get_ascii(i)
    for x in my_dic.values():
        my_list.append(x)
    my_list = list(set(my_list))
    for j in my_list:
        mini = []
        for k,v in my_dic.items():
             if v == j:
                 mini.append(k)
        words.append(mini)
    
    return words

def _get_ascii(s):
    value = 0
    for i in s:
        value += ord(i)
    return value 
            


print(anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
    
#!/usr/bin/python3
def isHappy(n):
    if n == 1:
        return 1
    s = []
    while _is_huppy(n) not in s:
        v = _is_huppy(n)
        if v == 1:
            return True
        else:
            s.append(v)
            n = v
    return False
def _is_huppy(n):
    value = 0
    while n>0:
        rem = n % 10
        n = n // 10
        value += rem ** 2
    return value   
           
    
    

print(isHappy(19))
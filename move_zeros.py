#!/usr/bin/python3
def zeros(a):
    value = 0
    inc = 0
    for i in range(len(a)):
        for j in range(0, len(a)-1):
            if a[j] == 0:
                temp = a[j]
                a[j] = a[j + 1]
                a[j+1] = temp
    return a

            



a = [2,8,0,6,1,0,0,8,0,2,0,9]
b = [0,1,0,3,12]
print(a)
print(zeros(a))
print(b)
print(zeros(b))
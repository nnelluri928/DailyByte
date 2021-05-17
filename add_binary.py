#!/usr/bin/env python3


def addBinary(a,b):
    
    i = len(a)-1
    j = len(b)-1
    c = 0
    res = []
    
    while i >= 0 or j >= 0 or c:
        total = c
        
        if i >=0:
            total += int(a[i])
            i -=1
        
        if j >=0:
            total += int(b[j])
            j -=1
        
        res.append(str(total % 2))
        c = total // 2
    return "".join(reversed(res))

a = '11'
b = '1'
print(addBinary(a,b))



def addBinary_1(a,b):
	return bin(int(a,2) + int(b,2))
a = '1010'
b = '1011'
print(addBinary(a,b))

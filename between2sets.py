#!/usr/local/bin/python3

a = [2]
b = [20, 30, 12]

def getTotalX(a, b):
    c1 = [] #Numbers between the 2 arrays to test
    c2 = [] #Numbers that are divisors of the lowest number of array 2
    c3 = [] #Numbers that are divisible by the first array
    r = min(b)
    s = max(a)
    for i in range(r+1):
        if i >= s:
            c1.append(i)
    for i in range(len(c1)):
        if r % c1[i] == 0:
            c2.append(c1[i])
        else:
            continue
    for ia in range(len(a)):
        for i in c2:
            if i % a[ia] == 0:
                c3.append(i)
            if i % a[ia] != 0:
                try:
                    c3.remove(i)
                except:
                    continue
    for ia in range(len(a)):
        for i in c2:
            if i % a[ia] != 0:
                try:
                    c3.remove(i)
                except:
                    continue    
    for ib in range(len(b)):
        for i in c3:
            if b[ib] % i != 0:
                try:
                    c3.remove(i)
                except:
                    continue
    for ib in range(len(b)):
        for i in c3:
            if b[ib] % i != 0:
                try:
                    c3.remove(i)
                except:
                    continue    
    c3 = set(c3)
    count = len(c3)
    return (count)
print (getTotalX(a, b))
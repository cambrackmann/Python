#!/usr/local/bin/python3
bill = [3, 10, 2, 9]
k = 1
b = 12

bill.remove(bill[k])
paid = int(sum(bill)/2)
b = int(b)

if paid == b:
    print ("Bon Appetit")
if paid != b:
    owed = b - paid
    print (owed)
#!/usr/local/bin/python3

def computepay(h,r):
    if h <= 40:
        p = h * r
    elif h > 40:
        p = 40 * r + float(h % 40) * (r * 1.5)
    return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Pay Rate:")
r = float(rate)

p = computepay(h,r)
print("Pay",p)

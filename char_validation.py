#!/usr/local/bin/python3

def char_valid():

    alphanum = False
    alpha = False
    digit = False
    lower = False
    upper = False
        
    for i in s:
        if alphanum is False and i.isalnum() is True:
            alphanum = True

        if alpha is False and i.isalpha() is True:
            alpha = True

        if digit is False and i.isdigit() is True:
            digit = True

        if lower is False and i.islower() is True:
            lower = True

        if upper is False and i.isupper() is True:
            upper = True

    tests = (alphanum, alpha, digit, lower, upper)
    return tests

results = char_valid()

for i in results:
    print(i)

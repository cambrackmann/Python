#!/usr/local/bin/python3
number = 17 

def print_formatted(number):
    spaces = (len((bin(number).replace("0b", "")))) + 1
    
    for i in range(number):
        num = i + 1
        octal = oct(i + 1).replace("0o", "")
        hexal = hex(i + 1).upper().replace("0X", "")
        binary = bin (i + 1).replace("0b", "")
        
        print (' '*(len(str(number)) - len(str(num))) + str(num) + (' '*(spaces - len(str(octal)))) + str(octal) + ' ' * (spaces - len(str(hexal))) + str(hexal) + ' ' * (spaces - len(str(binary))) + str(binary))
print_formatted(number)
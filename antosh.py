#!/usr/local/bin/python3

def remove_newline(input):
    var = input
    if var[-1:] == "\n":
        var = var[:-1]
    return var

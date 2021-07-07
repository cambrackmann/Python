#!/usr/local/bin/python3

max_width = 4
string_name = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def wrap(string_name, max_width):
    ret = ''

    for i in string_name:
        for i in range(0, len(string_name)):   
            if i % (max_width) == max_width - 1:
                ret += string_name[i] + "\n"
            else:
                ret += string_name[i]
        return ret 
if __name__ == '__main__':
    result = wrap(string_name, max_width)
    print (result)
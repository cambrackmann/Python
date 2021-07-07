#!/usr/local/bin/python3

# Alphabet Ragnoli

# print('-') == print('- \n', end = '')
# print('-') == print('-', end = '\n')

# a + 1 == b
# a + 2 == c
# A + 1 == B

def print_rangoli(size):
    vertical = 2 * size - 1
    horizontal = 2 * (2 * size -1) - 1
    ret=''
    middle_index = (horizontal - 1) / 2
    vertical_mid = (vertical - 1) / 2

    for v in range(vertical):
        for h in range(horizontal):
            if h == middle_index:
                middle_char = increment_character('a',  abs(size - v - 1))
                ret += middle_char
            elif h == 0 and v == (vertical - 1) / 2 or h == 2 * (2 * size -1) - 2 and v == (vertical - 1) /2:
                end_char = increment_character('a',  abs(size - 1))
                ret += end_char
            elif size > 2 and h == 2 and v == ((vertical - 1) / 2) - 1 or size > 2 and h == 2 * (2 * size -1) - 4 and v == ((vertical - 1) / 2) - 1:
                end_char = increment_character('a',  abs(size - 1))
                ret += end_char
            elif size > 2 and h == 2 and v == ((vertical - 1) / 2) + 1 or size > 2 and h == 2 * (2 * size -1) - 4 and v == ((vertical - 1) / 2) + 1:
                end_char = increment_character('a',  abs(size - 1))
                ret += end_char
            elif h == 2 and v == ((vertical - 1) / 2) or h == 2 * (2 * size -1) - 4 and v == ((vertical - 1) / 2):
                end_char = increment_character('a',  abs(size - 2))
                ret += end_char
# For Input = 4
            elif h == 4 and v == ((vertical - 1) / 2) - 2 or h == 2 * (2 * size -1) - 6 and v == ((vertical - 1) / 2) - 2:
                end_char = increment_character('a',  abs(size - 1))
                ret += end_char
            elif h == 4 and v == ((vertical - 1) / 2) + 2 or h == 2 * (2 * size -1) - 6 and v == ((vertical - 1) / 2) + 2:
                end_char = increment_character('a',  abs(size - 1))
                ret += end_char
            elif h == 4 and v == ((vertical - 1) / 2) - 1 or h == 2 * (2 * size -1) - 6 and v == ((vertical - 1) / 2) - 1:
                end_char = increment_character('a',  abs(size - 2))
                ret += end_char
            elif h == 4 and v == ((vertical - 1) / 2) + 1 or h == 2 * (2 * size -1) - 6 and v == ((vertical - 1) / 2) + 1:
                end_char = increment_character('a',  abs(size - 2))
                ret += end_char
            elif h == 4 and v == ((vertical - 1) / 2) or h == 2 * (2 * size -1) - 6 and v == ((vertical - 1) / 2):
                end_char = increment_character('a',  abs(size - 3))
                ret += end_char
# For Input = 5
            elif size > 3 and h == 6 and v == ((vertical - 1) / 2) - 2 or size > 3 and h == 2 * (2 * size -1) - 8 and v == ((vertical - 1) / 2) - 2:
                end_char = increment_character('a',  abs(size - 2))
                ret += end_char
            elif size > 3 and h == 6 and v == ((vertical - 1) / 2) + 2 or size > 3 and h == 2 * (2 * size -1) - 8 and v == ((vertical - 1) / 2) + 2:
                end_char = increment_character('a',  abs(size - 2))
                ret += end_char
            elif h == 6 and v == ((vertical - 1) / 2) - 1 or h == 2 * (2 * size -1) - 8 and v == ((vertical - 1) / 2) - 1:
                end_char = increment_character('a',  abs(size - 3))
                ret += end_char
            elif h == 6 and v == ((vertical - 1) / 2) + 1 or h == 2 * (2 * size -1) - 8 and v == ((vertical - 1) / 2) + 1:
                end_char = increment_character('a',  abs(size - 3))
                ret += end_char
            elif h == 6 and v == ((vertical - 1) / 2) or h == 2 * (2 * size -1) - 8 and v == ((vertical - 1) / 2):
                end_char = increment_character('a',  abs(size - 4))
                ret += end_char
            elif h == 6 and v == ((vertical - 1) / 2) + 3 or h == 2 * (2 * size -1) - 8 and v == ((vertical - 1) / 2) + 3:
                end_char = increment_character('a',  abs(size - 1))
                ret += end_char
            elif h == 6 and v == ((vertical - 1) / 2) - 3 or h == 2 * (2 * size -1) - 8 and v == ((vertical - 1) / 2) - 3:
                end_char = increment_character('a',  abs(size - 1))
                ret += end_char
            else:
                ret += '-'
        ret += '\n'
    print(ret)

def increment_character(input, value):
    # Increment given input character by the value amount
    # Ex: Input = A, Value = 2 -> return C
    i = ord(input[0])
    i += value
    return chr(i)

if __name__ == '__main__':
    print_rangoli(4)
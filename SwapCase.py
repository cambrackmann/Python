#!/usr/local/bin/python3

# a + 1 == b
# a + 2 == c
# A + 1 == B

string_name = "I Don't Like"

def swap_case(string_name):                                 # Defining fucnction named swap_case with string_name variable/input
    
    ret = ''                                                # Defining ret
    for element in string_name:                             # Element meaning each letter
        char_as_int = ord(element)                          # Defining a variable as the numerical value of each letter
        
        if char_as_int >= 65 and char_as_int <= 90:         # Numerical value of each letter from A to Z
            ret += chr(char_as_int + 32)                    # Adding to numerical value of each letter to get its undercase equivalent
        elif char_as_int >= 97 and char_as_int <= 122:      # Numerical value of each letter from a to z
            ret += chr(char_as_int - 32)                    # Subtracting value of each letter to get its uppercase equivalent
        else:
            ret += element                                  # If its not an uppercase or lowercase letter, not changing the element
    return ret

if __name__ == '__main__':
    result = swap_case(string_name)
    print (result)
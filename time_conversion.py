#!/usr/local/bin/python3

s = "11:59:59PM"

def timeConversion(s):

    if "PM" in s:
        s = s[:-2]
        if "12" not in s[:2]:
            h2 = str(int(s[1]) + 2)
            s = s.replace(s[1], h2, 1)
            if "1" in s[0]:
                s = s.replace("1", "2", 1)

        if "0" in s[0]:
            s = s.replace("0", "1", 1)
        elif "24" in s[:2]:
            s = s.replace("24", "00", 1)

    if "AM" in s:
        s = s[:-2]
        if "12" in s[:2]:
            s = s.replace("12", "00", 1)
    result = s
    return (result)

time_24 = timeConversion

print(time_24(s))
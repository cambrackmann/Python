#!/usr/local/bin/python3

size_of_set = int(input())
s = set(map(int, input().split()))
commands_to_execute = int(input())

while commands_to_execute is not 0:
    commands_to_execute -= 1
    cmd = str(input())

    if cmd != "pop":
        cmd, val = cmd.split()
        if cmd == "remove":
            try:
                s.remove(int(val))
            except:
                continue
        elif cmd == "discard":
            s.discard(int(val))
            
    elif cmd == "pop":
        # try pop from the set
        try:
            s.pop()
        except:
            continue

s_total = sum(s)
print(s_total)
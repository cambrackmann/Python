#!/usr/local/bin/python3

# The first line is the number of lines of names:
# 2
# Cameron
# Antoshka


num_of_names = int(input())
for i in range(num_of_names):
    name = input()
    print(name)

# The first line is the number of lines of full-names:
# 2
# Cameron Brackpoo
# Antoshka Milty

num_of_names = int(input())
for i in range(num_of_names):
    name = input().split()
    print(name)

# Similar to above, sometimes we simply do not need the 'num_of_names'
# 2
# Cameron Brackpoo
num_of_names = int(input())
name = input().split()
print(name)

# Split returns an array!
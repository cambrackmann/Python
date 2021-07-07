#!/usr/local/bin/python3

ar = [1, 3, 2, 6, 1, 2]
k = 3

end = len(ar)



count = 0
for i in range(len(ar)-1):
    ar1 = ar[i+1:end]
    for j in range(len(ar1)):
        add = ar[i] + ar1[j]
        print("add is", add)
        if add % k == 0:
            count += 1
print ("count is", count)
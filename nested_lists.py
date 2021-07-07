#!/usr/local/bin/python3

if __name__ == '__main__':
    n = int(input())
    names = []
    scores = []
    
    for i in range(n):
        names.append(input())
        scores.append(float(input()))

records = []
for i in range(n):
    student = []
    student.append(names[i])
    student.append(scores[i])
    records.append(student)
    
lowest_score = 100
for i in range(n):
    if records[i][1] < lowest_score:
        lowest_score = records[i][1]


for j in range(n):
    for i in range(n):
        try:
            if records[i][1] == lowest_score:
                del records[i]
        except:
            continue

lowest_score = 100
for i in range(len(records)):
    if records[i][1] < lowest_score:
        lowest_score = records[i][1]

lowest_scores = []
for i in range(len(records)):
    if records[i][1] == lowest_score:
        lowest_scores.append(records[i][0])
        
lowest_scores = sorted(lowest_scores)
for i in lowest_scores:
    print(i)
#!/usr/local/bin/python3
number = 17 

def checkMagazine(magazine, note):
    count = 0
    note1 = note
    
    for word in note1:
        if word in magazine:
            if note.count(word) <= magazine.count(word):
                count += 1
                note1.remove(word)
                magazine.remove(word)
            else:
                break
        else:
            break
                    
    if count == len(note):
        answer = 'Yes'
    else:
        answer = 'No'
        
    return answer
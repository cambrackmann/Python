#!/usr/local/bin/python3

x = 'no'
y = 0
z = 1
info = {}


while x != 'yes':

    data = input('Enter name & age separated by ":" ')
    x = input('Are you done? Enter "yes" or hit any key to continue: ')

    temp = data.split(':')

    info[temp[0]] = int(temp[1])


q = input('Would you like to see the dictionary? Enter yes or no: ')

if q == 'yes':
    for key, value in info.items():
        print('Name: {}, Age: {}'.format(key, value))


if q == 'no':
    print('All done!')
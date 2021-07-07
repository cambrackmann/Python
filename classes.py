#!/usr/local/bin/python3

class Dog:
    species = "Canis Familiaris"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.age} years old {self.breed}." 
    
x = ''

while x != 'no':
        
    dog_name = input("Enter dogs name: ")
    dog_age = input("Enter dogs age: ")
    dog_breed = input("Enter dogs breed: ")

    dog_name = Dog(dog_name, dog_age, dog_breed)

    x = input("To add more dogs, press any key.  To finish, enter 'no'. \n ")

x = input("Would you like to see the information of a dog? Enter 'yes' or 'no' \n ")


if x == 'no':
    exit

if x == 'yes':


    while x == 'yes':

        search = input("Which dog would you like to know more about? \n ")
        dog = Dog.__str__(search)

        print(dog)

        y = input("To look up another dog, press any key. To end search, enter 'done'. \n ")

        if y == 'done':
            x = y
        
        else:
            continue
#!/usr/local/bin/python3

# Set contains only keys:
people_in_class = set()
people_in_class.add("Cameron")
people_in_class.add("Antoshka")

for person in people_in_class:
    print(f"class contains: {person}")

# Dictionary contains key-value pairs

people_ages = {}
people_ages["Cameron"] = 24
people_ages["Antoshka"] = 27

for person in people_ages:
    print(f"Person: {person} aged: {people_ages[person]}")

# Dictionaries can contain other structures
# Example of a dictionary containing array values

people_attributes = {}
people_attributes["Cameron"] = ["super handsome", "24 years old", "smarty"]
people_attributes["Antoshka"] = ["super handsome", "27 years old", "one lucky boy"]

# Iterating over a dictionary:

for person in people_attributes:
    print(f"Person: {person} values: {people_attributes[person]}")

# Add the people to the dictionary:
people = ["Cam", "Antosh"]

peoples_ages = {}

for person in people:
    peoples_ages[person] = 0

# Add some ages:
peoples_ages["Antosh"] = 27
peoples_ages["Cam"] = 24

# Cam has had a birthday. Let's first check if he exists in the dict, then increase his age by 1:
if "Cam" in peoples_ages:
    peoples_ages["Cam"] += 1

# Let's find the people who have a birthday of 25!
for person in peoples_ages:
    if peoples_ages[person] == 25:
        print(f"{person} is 25!")
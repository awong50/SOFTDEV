"""
Aidan Wong
Elmos_Cheez-it
SoftDev
05_bitsream
2024-09-17
time spent: 0.5
"""

f = open("krewes.txt", "r")
people = f.read().replace("\n", "").split('@@@')
for count, person in enumerate(people):
    people[count] = person.split('$$$')
    person = {people[count][0], people[count][1], people[count][2]}

print(people)
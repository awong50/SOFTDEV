"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K05 -- Bitstream
2024-09-17
time spent: 0.5
"""

import random

f = open("krewess.txt", "r")
people = f.read().replace("\n", "").split('@@@') # Splitting this way has issues with intended values of @ and $, .split() can be used instead of .replace()
people = people[:len(people)-1]
for count, person in enumerate(people): # Enumerate works as the counter
    people[count] = person.split('$$$') 
    people[count] = {"period":people[count][0], "devo":people[count][1], "ducky":people[count][2]} # Add dictionary to people list at count

randoDevo = random.randint(0, len(people)-1) # Select random existing position from people list

print("Name: " + people[randoDevo].get("devo") + " | Period: " + people[randoDevo].get("period") + " | Ducky: " + people[randoDevo].get("ducky")) # Final print statement to get random devo information

"""
print(people)

#Lets say you want to know all of the people/duckys in period 4
p4Peeps = []
p4Duckys = []
for person in people:
    if person.get("period") == '05':
        p4Peeps.append(person.get("devo"))
        p4Duckys.append(person.get("ducky"))
print(p4Peeps)
print(p4Duckys)
"""
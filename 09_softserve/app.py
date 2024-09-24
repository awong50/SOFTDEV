"""
Aidan Wong
Clueless
SoftDev
K09 - Exploring Flask
2024-09-23
time spent: 0
"""

import random

with open("occupations.csv") as file: # Open file with this method so it closes by itself
    data = file.read().strip().split("\n")

occupation = {}
weights = []

for i in range(1, len(data)-1):
    splitted = data[i].rsplit(",", 1) # Split by first comma from the right 
    splitted[0] = splitted[0].replace('"', "") # Remove quotes if present
    occupation[splitted[0]] = splitted[1] # Add to dictionary
    weights.append(float(splitted[1])) # Append weight value to weight list

randO = random.choices(list(occupation), weights, k=1)

print("Random Occupation: " + str(randO[0]) + " | " + "Occupation Weight: " + occupation[str(randO[0])])



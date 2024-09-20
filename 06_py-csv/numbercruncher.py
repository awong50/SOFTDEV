"""
Aidan Wong
Mac_N_Cheez-its
SoftDev
K06 - Reading CSV files
2024-09-19
time spent: 1.0

DISCO: Keys of dict = Job class; Use int() to convert % into integers; use .split(",") to seperate values in table

QCC: First and last items don't go into dictionary; Commas appear in quotations (use those to split); How to randomly select by weight

HOW THIS SCRIPT WORKS: Read occupations.csv and assign it to "data", stripping it and splitting it by new line; Iterate through "data" and replace commas inside quotations with "<>" to preserve them; Iterate through "data" again, splitting it by commas to get the key and value (the key being the occupation name and the value being the weight), after splitting replace "<>" with commas and quotes with empty strings, finally adding it to the dictionary and appending the weight value to a weights list, Randomly select random occupation (either with random.choices() or custom method below), print random occupation
"""

# OPTIMIZED CODE AFTER DEMOS

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

# ORIGINAL CODE
"""

import random

with open("occupations.csv") as file: # Open file with this method so it closes by itself
    data = file.read().strip().split("\n")

occupation = {}
weights = []

for i in range(1, len(data)-1):
    job = data[i]
    if job[0]=='"': # Look for quotations and replace commas with placeholder inside them
        key = job[1:].index('"')
        temp = job[0:key].replace(",","<>") + job[key:] # replacing necessary comma with placeholder
        data[i] = temp # Assign the value with the placeholder to data

for i in range(1, len(data)-1):
    splitted = data[i].split(",") # Split by comma (reason why commas were replaced within the quotations before -- in order to preserve and not split those commas)
    splitted[0] = splitted[0].replace("<>", ",").replace('"',"") # replacing placeholder with comma and removing the quotes
    occupation[splitted[0]] = splitted[1] # Add to dictionary
    weights.append(float(splitted[1])) # Append weight value to weight list

# Logic to select a random occupation with weights: Iterate through weights list and keeps track of a culmative value. If adding a specific weight causes it to exceed the randomly generated value, it will print that as the random occupation
for i in range (0, 1000): # Inside a for loop to do many testings quickly
    total_weight = sum(weights)
    culmative_weight = 0          
    randomVal = random.uniform(0, total_weight) # random.uniform to include float numbers
    randO = None # Assigned to None for no value

    for i, weight in enumerate(weights): # For loop that checks with the culmative value
        culmative_weight += weight 
        if randomVal <= culmative_weight:
            randO = list(occupation.keys())[i] # Turns the occupations.keys() object to a list to select the ith value from it (as the weights list and dictionary key values are aligned -- occupation corresponds to weight)
            break # Break to prevent the for loop to continue running and always select the last key in dictionary
    print(randO)
 

"""



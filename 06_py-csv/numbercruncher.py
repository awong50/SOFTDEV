"""
Aidan Wong
Mac_N_Cheez-its
SoftDev
K06 - Reading CSV files
2024-09-19
time spent:

DISCO:

QCC:

HOW THIS SCRIPT WORKS:
"""

import random

occupationDict = {}
f = open("occupations.csv", "r")
occupations = f.read().strip().split("\n")
for _ in range(1, len(occupations) - 1):
    job = occupations[_]
    if job[0] == '""':
        key = job[1:].index('""')
        tmp = job[0:key].replace(",", "<>") + job[key:]
        occupations[_] = tmp

print(occupations)
    
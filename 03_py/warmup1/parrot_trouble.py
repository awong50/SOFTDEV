"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Simple, no loops)
2024-09-11
time spent: 0.02
"""

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7)) 
print(parrot_trouble(False, 6)) 
print(parrot_trouble(True, 21)) 
print(parrot_trouble(False, 21)) 
print(parrot_trouble(False, 20)) 
print(parrot_trouble(True, 23)) 
print(parrot_trouble(False, 23)) 	
print(parrot_trouble(True, 20)) 
print(parrot_trouble(False, 12))
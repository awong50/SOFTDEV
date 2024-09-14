"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Simple, no loops)
2024-09-12
time spent: 0.04
"""

def front_back(str):
  if len(str) == 1:
    return str
  return str[len(str) - 1: len(str)] + str[1:len(str) - 1] + str[0: 1]

print(front_back('code')) 
print(front_back('a')) 
print(front_back('ab')) 
print(front_back('abc')) 
print(front_back(''))
print(front_back('Chocolate')) 
print(front_back('aavJ')) 	
print(front_back('hello'))
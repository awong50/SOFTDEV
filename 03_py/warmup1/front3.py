"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def front3(str):
  if len(str) < 3:
    return str * 3
  return str[0:3] * 3

print(front3('Java')) 
print(front3('Chocolate')) 	
print(front3('abc')) 	
print(front3('abcXYZ'))
print(front3('ab'))
print(front3('a'))	
print(front3(''))
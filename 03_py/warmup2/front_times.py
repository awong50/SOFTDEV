"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Medium, With loops)
2024-09-12
time spent: 0.02
"""

def front_times(str, n):
  if len(str) < 3:
    return str * n
  return str[0:3] * n

print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3)) 
print(front_times('Abc', 3))
print(front_times('Ab', 4))
print(front_times('A', 4)) 
print(front_times('', 4))
print(front_times('Abc', 0))
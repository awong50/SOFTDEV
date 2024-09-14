"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Simple, no loops)
2024-09-11
time spent: 0.02
"""

def makes10(a, b):
  return a == 10 or b == 10 or a + b == 10
  
print(makes10(9, 10)) 
print(makes10(9, 9)) 
print(makes10(1, 9)) 
print(makes10(10, 1)) 
print(makes10(10, 10)) 
print(makes10(8, 2))
print(makes10(8, 3)) 
print(makes10(10, 42)) 
print(makes10(12, -2))
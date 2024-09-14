"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Simple, no loops)
2024-09-11
time spent: 0.02
"""

def diff21(n):
  if n > 21:
    return 2 * abs(n - 21)
  return abs(n - 21)


print(diff21(19))
print(diff21(10)) 
print(diff21(21))
print(diff21(22)) 
print(diff21(25))	
print(diff21(30)) 
print(diff21(0)) 
print(diff21(1)) 
print(diff21(2)) 
print(diff21(-1)) 
print(diff21(-2)) 
print(diff21(50)) 
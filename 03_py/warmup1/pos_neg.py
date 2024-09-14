"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  return (a * b) < 0

print(pos_neg(1, -1, False)) 	
print(pos_neg(-1, 1, False)) 	
print(pos_neg(-4, -5, True)) 	
print(pos_neg(-4, -5, False)) 
print(pos_neg(-4, 5, False)) 	
print(pos_neg(-4, 5, True)) 
print(pos_neg(1, 1, False)) 
print(pos_neg(-1, -1, False)) 
print(pos_neg(1, -1, True)) 
print(pos_neg(-1, 1, True)) 
print(pos_neg(1, 1, True)) 
print(pos_neg(-1, -1, True)) 	
print(pos_neg(5, -5, False)) 	
print(pos_neg(-6, 6, False)) 	
print(pos_neg(-5, -6, False)) 
print(pos_neg(-2, -1, False)) 
print(pos_neg(1, 2, False)) 
print(pos_neg(-5, 6, True)) 
print(pos_neg(-5, -5, True))

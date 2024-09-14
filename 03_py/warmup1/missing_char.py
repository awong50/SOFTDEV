"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Simple, no loops)
2024-09-12
time spent: 0.1
"""

def missing_char(str, n):
  return str[0:n] + str[n + 1:len(str)]

print(missing_char('kitten', 1)) 	
print(missing_char('kitten', 0)) 	
print(missing_char('kitten', 4)) 
print(missing_char('Hi', 0)) 
print(missing_char('Hi', 1)) 
print(missing_char('code', 0))
print(missing_char('code', 1))
print(missing_char('code', 2)) 
print(missing_char('code', 3)) 
print(missing_char('chocolate', 8))
"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def not_string(str):
  if str[0:3] == "not":
    return str
  return "not " + str

print(not_string('candy'))
print(not_string('x')) 	
print(not_string('not bad'))
print(not_string('bad')) 
print(not_string('not'))
print(not_string('is not')) 
print(not_string('no'))
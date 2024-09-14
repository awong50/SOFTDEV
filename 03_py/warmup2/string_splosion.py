"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Medium, With loops)
2024-09-12
time spent: 0.03
"""

def string_splosion(str):
  newstr = ""
  for _ in range(len(str)):
    newstr += str[0:_ + 1]
  return newstr

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
print(string_splosion('x'))
print(string_splosion('fade'))
print(string_splosion('There'))
print(string_splosion('Kitten'))
print(string_splosion('Bye'))
print(string_splosion('Good'))
print(string_splosion('Bad'))
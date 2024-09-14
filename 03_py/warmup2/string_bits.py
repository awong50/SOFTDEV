"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Medium, With loops)
2024-09-12
time spent: 0.01
"""

def string_bits(str):
  newstr =""
  for _ in range(len(str)):
    if _ % 2 == 0:
      newstr += str[_]
  return newstr

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
print(string_bits('HiHiHi'))
print(string_bits(''))
print(string_bits('Greetings'))
print(string_bits('Chocoate'))
print(string_bits('pi'))
print(string_bits('Hello Kitten'))
print(string_bits('hxaxpxpxy'))
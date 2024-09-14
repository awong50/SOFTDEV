"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Medium, With loops)
2024-09-12
time spent: 0.05
"""

def last2(str):
  checkstr = str[len(str) - 2: len(str)]
  count = 0
  for _ in range(len(str) - 2):
    if str[_:_+2] == checkstr:
      count += 1
  return count

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print(last2('xxaxxaxxaxx'))
print(last2('xaxaxaxx'))	
print(last2('xxxx'))
print(last2('13121312'))
print(last2('11212'))	
print(last2('13121311'))
print(last2('1717171'))
print(last2('hi'))	
print(last2('h'))
print(last2(''))
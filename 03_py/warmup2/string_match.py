"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Medium, With loops)
2024-09-12
time spent: 0.03
"""

def string_match(a, b):
  count = 0
  for _ in range(len(a) - 1):
    if a[_:_+2] == b[_:_+2]:
      count += 1
  return count


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
print(string_match('hello', 'he'))
print(string_match('he', 'hello'))
print(string_match('h', 'hello'))
print(string_match('', 'hello'))
print(string_match('aabbccdd', 'abbbxxd'))
print(string_match('aaxxaaxx', 'iaxxai'))
print(string_match('iaxxai', 'aaxxaaxx'))
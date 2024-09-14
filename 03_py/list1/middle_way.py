"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def middle_way(a, b):
  return [a[1], b[1]]

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))
print(middle_way([1, 9, 7], [4, 8, 8]))
print(middle_way([1, 2, 3], [3, 1, 4]))
print(middle_way([1, 2, 3], [4, 1, 1]))
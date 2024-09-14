"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def common_end(a, b):
  return a[len(a) - 1] == b[len(b) - 1] or a[0] == b[0]

print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))
print(common_end([1, 2, 3], [1]))
print(common_end([1, 2, 3], [2]))
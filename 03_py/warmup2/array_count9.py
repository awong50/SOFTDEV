"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Medium, With loops)
2024-09-12
time spent: 0.02
"""

def array_count9(nums):
  count = 0
  for _ in nums:
    if _ == 9:
      count += 1
  return count

print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))
print(array_count9([1, 2, 3]))
print(array_count9([]))
print(array_count9([4, 2, 4, 3, 1]))
print(array_count9([9, 2, 4, 3, 1]))
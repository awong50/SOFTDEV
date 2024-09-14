"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Medium, With loops)
2024-09-12
time spent: 0.02
"""

def array_front9(nums):
  for _ in range(min(4, len(nums))):
    if nums[_] == 9:
      return True
  return False

print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))
print(array_front9([9, 2, 3]))
print(array_front9([1, 9, 9]))
print(array_front9([1, 2, 3]))
print(array_front9([1, 9]))
print(array_front9([5, 5]))
print(array_front9([2]))
print(array_front9([9]))
print(array_front9([]))
print(array_front9([3, 9, 2, 3, 3]))
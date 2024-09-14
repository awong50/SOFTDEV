"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Medium, One Loop)
2024-09-12
time spent: 0.04
"""

def has22(nums):
  for _ in range(len(nums) - 1):
    if nums[_] == nums[_ + 1] and nums[_] == 2:
      return True
  return False

print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))
print(has22([2, 2, 1, 2]))
print(has22([1, 3, 2]))
print(has22([1, 3, 2, 2]))
print(has22([2, 3, 2, 2]))
print(has22([4, 2, 4, 2, 2, 5]))
print(has22([1, 2]))
print(has22([2, 2]))
print(has22([2]))
print(has22([]))
print(has22([3, 3, 2, 2]))
print(has22([5, 2, 5, 2]))
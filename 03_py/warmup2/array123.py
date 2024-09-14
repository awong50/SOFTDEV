"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python (Medium, With loops)
2024-09-12
time spent: 0.1
"""

def array123(nums):
  for _ in range(len(nums) - 2):
    if nums[_] == 1 and nums[_ + 1] == 2 and nums[_ + 2] == 3:
      return True
  return False
  
print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
print(array123([1, 1, 2, 1, 2, 1]))
print(array123([1, 2, 3, 1, 2, 3]))
print(array123([1, 2, 3]))
print(array123([1, 1, 1]))
print(array123([1, 2]))
print(array123([1]))
print(array123([]))
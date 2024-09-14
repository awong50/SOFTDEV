"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def same_first_last(nums):
  return len(nums) > 0 and nums[0] == nums[len(nums) - 1]

print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))
print(same_first_last([7]))
print(same_first_last([]))
print(same_first_last([1, 2, 3, 4, 5, 1]))
print(same_first_last([1, 2, 3, 4, 5, 13]))	
print(same_first_last([13, 2, 3, 4, 5, 13]))	
print(same_first_last([7, 7]))
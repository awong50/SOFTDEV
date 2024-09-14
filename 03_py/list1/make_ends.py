"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def make_ends(nums):
  return [nums[0], nums[len(nums) - 1]]

print(make_ends([1, 2, 3]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))
print(make_ends([1, 2, 2, 2, 2, 2, 2, 3]))	
print(make_ends([7, 4]))
print(make_ends([7]))
print(make_ends([5, 2, 9]))
print(make_ends([2, 3, 4, 1]))
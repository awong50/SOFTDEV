"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Simple, no loops)
2024-09-12
time spent: 0.1
"""

def max_end3(nums):
  maxVal = max(nums[0], nums[len(nums) - 1])
  for _ in range(len(nums)):
    nums[_] = maxVal
  return nums

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))
print(max_end3([11, 3, 3]))
print(max_end3([3, 11, 11]))
print(max_end3([2, 2, 2]))
print(max_end3([2, 11, 2]))
print(max_end3([0, 0, 1]))
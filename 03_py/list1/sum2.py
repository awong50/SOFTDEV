"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) < 2:
    return nums[0]
  return nums[0] + nums[1]

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))
print(sum2([1, 2]))
print(sum2([1]))
print(sum2([]))
print(sum2([4, 5, 6]))
print(sum2([4]))
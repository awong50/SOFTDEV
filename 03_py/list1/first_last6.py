"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Simple, no loops)
2024-09-12
time spent: 0.02
"""

def first_last6(nums):
  return nums[0] == 6 or nums[len(nums) - 1] == 6

print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 6]))
print(first_last6([3, 2, 1]))
print(first_last6([3, 6, 1]))
print(first_last6([3, 6]))
print(first_last6([6]))
print(first_last6([3]))
print(first_last6([5, 6]))
print(first_last6([5, 5]))
print(first_last6([1, 2, 3, 4, 6]))
print(first_last6([1, 2, 3, 4]))
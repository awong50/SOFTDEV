"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Medium, One Loop)
2024-09-12
time spent: 0.02
"""

def big_diff(nums):
  return max(nums) - min(nums)

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))
print(big_diff([2, 10]))
print(big_diff([10, 2]))
print(big_diff([10, 0]))
print(big_diff([2, 3]))
print(big_diff([2, 2]))
print(big_diff([2]))
print(big_diff([5, 1, 6, 1, 9, 9]))
print(big_diff([7, 6, 8, 5]))
print(big_diff([7, 7, 6, 8, 5, 5, 6]))
"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Medium, One Loop)
2024-09-12
time spent: 0.12
"""

def sum13(nums):
  count = 0
  skip = False
  for _ in range(len(nums)):
    if nums[_] == 13:
      if _ + 1 < len(nums) and nums[_ + 1] != 13:
        count -= nums[_ + 1]
      continue
    count += nums[_]
  return count

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))
print(sum13([1, 2, 13, 2, 1, 13]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))
print(sum13([]))
print(sum13([13]))
print(sum13([13, 13]))
print(sum13([13, 0, 13]))
print(sum13([13, 1, 13]))
print(sum13([5, 7, 2]))
print(sum13([5, 13, 2]))
print(sum13([0]))
print(sum13([13, 0]))
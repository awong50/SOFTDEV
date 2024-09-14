"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Medium, One Loop)
2024-09-12
time spent: 0.04
"""

def count_evens(nums):
  count = 0
  for _ in range(len(nums)):
    if nums[_] % 2 == 0:
      count += 1
  return count

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
print(count_evens([]))
print(count_evens([11, 9, 0, 1]))
print(count_evens([2, 11, 9, 0]))
print(count_evens([2]))
print(count_evens([2, 5, 12]))
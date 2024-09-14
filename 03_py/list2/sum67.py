"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Medium, One Loop)
2024-09-12
time spent: 0.15
"""

def sum67(nums):
  count = True
  counter = 0
  for _ in range(len(nums)):
    if nums[_] == 6:
      count = False
      continue
    if not count and nums[_] == 7:
      count = True
      continue
    if count:
      counter += nums[_]
  return counter

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))	
print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))	
print(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))
print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))
print(sum67([2, 7, 6, 2, 6, 2, 7]))
print(sum67([1, 6, 7, 7]))
print(sum67([6, 7, 1, 6, 7, 7]))
print(sum67([6, 8, 1, 6, 7]))
print(sum67([]))
print(sum67([6, 7, 11]))
print(sum67([11, 6, 7, 11]))
print(sum67([2, 2, 6, 7, 7]))
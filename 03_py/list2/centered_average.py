"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Medium, One Loop)
2024-09-12
time spent: 0.08
"""

def centered_average(nums):
  nums.sort()
  return sum(nums[1:-1]) / (len(nums) - 2)

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
print(centered_average([5, 3, 4, 6, 2]))
print(centered_average([5, 3, 4, 0, 100]))
print(centered_average([100, 0, 5, 3, 4]))
print(centered_average([4, 0, 100]))
print(centered_average([0, 2, 3, 4, 100]))
print(centered_average([1, 1, 100]))
print(centered_average([7, 7, 7]))
print(centered_average([1, 7, 8]))
print(centered_average([1, 1, 99, 99]))
print(centered_average([1000, 0, 1, 99]))
print(centered_average([4, 4, 4, 4, 5]))
print(centered_average([4, 4, 4, 1, 5]))
print(centered_average([6, 4, 8, 12, 3]))
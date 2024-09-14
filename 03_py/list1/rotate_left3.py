"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K03 -- Review Python Lists (Simple, no loops)
2024-09-12
time spent: 0.1
"""

def rotate_left3(nums):
  return nums[1:] + nums[:1]

print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))
print(rotate_left3([1, 2, 1]))	
print(rotate_left3([0, 0, 1]))
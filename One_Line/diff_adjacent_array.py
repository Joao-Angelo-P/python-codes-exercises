# 3423. Maximum Difference Between Adjacent Elements in a Circular Array
class Solution:
    maxAdjacentDistance = lambda self, nums: max(
        map(lambda t: abs(t[1] - nums[t[0] - 1]), enumerate(nums))
    )

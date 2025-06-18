# 1107 case -> Time Limit Exceeded (FIX)
class Solution:
    divideArray = lambda self, nums, k: (
        arr
        if nums.sort() is None
        and (
            arr := [
                nums[i : i + 3]
                for i in range(0, len(nums), 3)
                if nums[i + 2] - nums[i] <= k
            ]
        )
        and len(arr) * 3 == len(nums)
        else []
    )

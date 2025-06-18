# 1107 case -> Time Limit Exceeded
class Solution:
    divideArray = lambda self, nums, k: (
        [
            sorted(nums)[i : i + 3]
            for i in range(0, len(sorted(nums)), 3)
            if sorted(nums)[i + 2] - sorted(nums)[i] <= k
        ]
        if len(
            [
                sorted(nums)[i : i + 3]
                for i in range(0, len(sorted(nums)), 3)
                if sorted(nums)[i + 2] - sorted(nums)[i] <= k
            ]
        )
        == len(nums) // 3
        else []
    )

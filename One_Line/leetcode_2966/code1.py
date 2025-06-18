"""
The decorator is for sorting list before insert it in divideArray function, but still one line solution.
Without the decorator, this program don't pass all the tests. It stuck in "Time Limit Exceeded" exception.
*The 'code2.py' is the code without decorator*.
"""


class Solution:
    def d_sort(f):
        def wrap(*args, **kw):
            args[1].sort()
            l = len(args[1])
            # self.c = self.l//3
            return f(l=l, *args, **kw)

        return wrap

    # self, nums: List[int], k: int
    divideArray = lambda self, nums, k, l: (
        arr
        if (
            arr := [
                nums[i : i + 3] for i in range(0, l, 3) if nums[i + 2] - nums[i] <= k
            ]
        )
        and len(arr) * 3 == len(nums)
        else []
    )

    divideArray = d_sort(divideArray)

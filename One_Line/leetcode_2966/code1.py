"""
The decorator is for sorting list before insert it in divideArray function, but still one line solution.
Without the decorator, this program don't pass all the tests. It stuck in "Time Limit Exceeded" exception.
*The 'code2.py' is the code without decorator*.
"""


class Solution:
    def d_sort(f):
        def wrap(*args, **kw):
            self_, nums_ = args[:2]
            nums_.sort()
            self_.l = len(nums_)
            # self.c = self.l//3
            return f(*args, **kw)

        return wrap

    # self, nums: List[int], k: int
    divideArray = lambda self, nums, k: (
        arr
        if (
            arr := [
                nums[i : i + 3] for i in range(0, self.l, 3) if nums[i + 2] - nums[i] <= k
            ]
        )
        and len(arr) * 3 == self.l
        else []
    )

    divideArray = d_sort(divideArray)

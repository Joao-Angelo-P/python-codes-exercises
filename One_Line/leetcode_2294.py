"""
Code from: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/solutions/6855596/one-line-solution
"""
class Solution:
    def d_sorted(func):
        def wrap(*args):
            nums_ = args[1]
            nums_.sort()
            return func(*args)

        return wrap

    partitionArray = lambda self, nums, k: len(
        {*accumulate(nums, lambda q, v: (q, v)[v - q > k])}
    )

    partitionArray = d_sorted(partitionArray)

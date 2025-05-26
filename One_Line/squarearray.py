# 977. Squares of a Sorted Array
class Solution:
    sortedSquares = lambda self, nums: sorted(map(lambda j: j**2, nums))

class Solution:
    findNumbers = lambda self, nums: len(
        tuple(filter(lambda i: len(str(i)) % 2 == 0, nums))
    )

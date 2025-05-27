# 2894. Divisible and Non-divisible Sums Difference
class Solution:
    differenceOfSums = lambda self, n, m: sum(
        filter(lambda x: x % m, range(1, n + 1))
    ) - sum(filter(lambda x: not x % m, range(1, n + 1)))

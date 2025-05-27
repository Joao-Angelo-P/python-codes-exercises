# 2894. Divisible and Non-divisible Sums Difference
class Solution:
    differenceOfSums = lambda self, n, m: sum(
        i if i % m else -i for i in range(1, n + 1)
    )

# 2894. Divisible and Non-divisible Sums Difference
class Solution:
    differenceOfSums = lambda self, n, m: sum(
        i if i % m else -i for i in range(1, n + 1)
    )


class Solution:
    differenceOfSums = lambda self, n, m: sum(
        [*range(1, n + 1), *[*range(-m, -n - 1, -m)] * 2]
    )


#3024. Type of Triangle
class Solution: triangleType= lambda self, nums: "none" if sum(sorted(nums)[:2]) <= sorted(nums)[-1] else {1:"equilateral", 2:"isosceles", 3:"scalene"}[len({*nums})]
class Solution: triangleType= lambda self, nums: ["none", "equilateral", "isosceles", "scalene"][(sum(sorted(nums)[:2]) > sorted(nums)[-1]) * len({*nums})]

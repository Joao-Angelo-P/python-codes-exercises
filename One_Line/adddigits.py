#258. Add Digits
class Solution: addDigits=lambda self, num: self.addDigits(sum(divmod(num, 10))) if num >= 10 else num
Solution = type("Solution", (), dict(addDigits=lambda self, num: self.addDigits(num%10+num//10) if num >= 10 else num))

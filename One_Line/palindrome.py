def filtrar(func):
    def _wrap(*args):
        if args[0].bool_:
            if args[1] % 10 == 0 and args[1] or args[1] < 0:
                return False
            args[0].bool_ = False
            # args[0].num = args[1]
            args[0].rev = 0
        return func(*args)

    return _wrap


class Solution:
    bool_ = True
    isPalindrome = lambda self, x: (
        self.isPalindrome(x // 10)
        if x and setattr(self, "rev", self.rev * 10 + x % 10) is None
        else x in (self.rev, self.rev//10)
    )
    isPalindrome = filtrar(isPalindrome)

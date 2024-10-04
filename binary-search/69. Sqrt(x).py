# type: ignore

class Solution:
    def mySqrt(self, x: int) -> int:
        # find n that n^2 <= x
        x += 1
        l = 0
        r = x // 2 + 1

        while l < r:
            m = l + (r - l) // 2

            if m*m < x:
                l = m + 1
            else:
                r = m
        return l - 1


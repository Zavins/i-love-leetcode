# type: ignore

class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1/x

        res = 1
        while n:
            if n & 1 == 1:
                res *= x
            
            x *= x
            #shift by 1 bit
            n = n >> 1
        
        return res


#x * x = x^2
#x^2 * x^2 = x^4
#x^4 * x^4 = x^8
#x^4 * x^8 * x

# 13 = 1101

# res *= x
# x = x * x
# type: ignore

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                self.make_zero(digits, i+1)
                return digits

        digits = [1] + digits
        self.make_zero(digits, 1)
        return digits
    
    def make_zero(self, digits, i):
        while i < len(digits):
            digits[i] = 0
            i += 1
# type: ignore

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        min_count = 0
        max_count = 0

        for i in range(len(s)):
            if locked[i] == "1":
                if s[i] == "(":
                    min_count += 1
                    max_count += 1
                elif s[i] == ")":
                    min_count -= 1
                    max_count -= 1
            elif locked[i] == "0":
                min_count -= 1
                max_count += 1
            
            if max_count < 0:
                return False
            
            if min_count < 0:
                min_count += 2
            
        return min_count == 0
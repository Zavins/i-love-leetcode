# type: ignore

class Solution:
    def checkValidString(self, s: str) -> bool:
        max_count = 0 # unmatched left parethesis, if all * are (
        min_count = 0 # unmatched right parenthesis if all * are )
        for c in s:
            if c == "(":
                max_count += 1
                min_count += 1
            elif c == ")":
                max_count -= 1
                min_count -= 1
            elif c == "*":
                max_count += 1
                min_count -= 1

            if max_count < 0:
                return False
            
            if min_count < 0:
                min_count = 0

        return min_count == 0

# type: ignore

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n*2:
                return [s]
            res = []
            if left < n:
                res += dfs(left + 1, right, s + '(')
            
            if right < left:
                res += dfs(left, right + 1, s + ')')

            return res

        return dfs(0, 0, "")
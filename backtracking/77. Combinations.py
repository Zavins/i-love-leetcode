# type: ignore

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(m, arr):
            if len(arr) == k:
                return [arr]
            
            if m > n:
                return []
            
            res = []
            for i in range(m, n + 1):
                res += backtrack(i+1, arr + [i])
            return res
        return backtrack(1, [])
            
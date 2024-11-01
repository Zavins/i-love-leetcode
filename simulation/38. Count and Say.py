# type: ignore

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n-1):
            res = self.rle_encode(res)
        return res

    def rle_encode(self, s):
        count = 1
        res = []
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res.append(f"{count}{s[i-1]}")
                count = 1
            else:
                count += 1
        res.append(f"{count}{s[-1]}")
        return "".join(res)
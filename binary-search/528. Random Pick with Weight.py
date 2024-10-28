# type: ignore

class Solution:

    def __init__(self, w: List[int]):

        # O(n)
        self.prefix_sum = []
        
        self.total = 0
        for i in w:
            self.total += i
            self.prefix_sum.append(self.total)

    def pickIndex(self) -> int:
        # binary search
        # O(log n)
        num = random.uniform(0, self.total)
        l = 0
        r = len(self.prefix_sum)

        while l < r:
            m = l + (r - l) // 2

            if self.prefix_sum[m] < num:
                l = m + 1
            else:
                r = m
        
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
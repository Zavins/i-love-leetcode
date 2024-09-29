# type: ignore
from collections import Counter

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        c = [l[0] / l[1] for l in rectangles]

        d = Counter(c)

        res = 0
        for v in d.values():
            res += v*(v-1) // 2
    
        return res
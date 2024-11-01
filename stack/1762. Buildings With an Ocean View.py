# type: ignore


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # res = []

        # m = 0

        # for i in range(len(heights)-1, -1, -1):
        #     if heights[i] > m:
        #         m = heights[i]
        #         res.append(i)
        
        # res.reverse()
        # return res

        # decreasing monotonic stack
        d = Deque()

        for i in range(len(heights)):
            while d and d[-1][0] <= heights[i]:
                d.pop()
            
            d.append((heights[i], i))

        return [item[1] for item in d]
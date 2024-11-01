# type: ignore

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        d = Deque()

        arr = [0]* len(heights)

        for i in range(len(heights)):
            while d and heights[i] >= d[-1][0]:
                height, index = d.pop()
                arr[index] += 1
            
            if d:
                index = d[-1][1]
                arr[index] += 1
            d.append((heights[i], i))
        
        return arr
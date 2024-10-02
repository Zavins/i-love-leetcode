# type: ignore
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr = sorted(zip(difficulty, profit))
        profit_arr = [0] * len(arr)
        max_p = 0
        for i in range(len(arr)):
            d, p = arr[i]
            max_p = max(max_p, p)
            profit_arr[i] = (d, max_p)
        
        res = 0

        for i in worker:
            index = self.bin_search(profit_arr, i+1)-1
            if index < 0:
                continue
            res += profit_arr[index][1]
        return res

    def bin_search(self, profit_arr, find):
        l = 0
        r = len(profit_arr)
        while l < r:
            m = l + (r - l ) // 2
            if find > profit_arr[m][0]:
                l = m + 1
            else:
                r = m
        return l
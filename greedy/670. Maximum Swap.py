# type: ignore

class Solution:
    def maximumSwap(self, num: int) -> int:
        last_i = [-1] * 10
        s = list(str(num))

        for i in range(len(s)):
            last_i[int(s[i])] = i
        

        for i in range(len(s)):
            c = s[i]
            for j in range(9, int(c), -1):
                if last_i[j] > i:
                    print(last_i[j], i)
                    s[i], s[last_i[j]] = s[last_i[j]], s[i]
                    return int(''.join(s))
        
        return num
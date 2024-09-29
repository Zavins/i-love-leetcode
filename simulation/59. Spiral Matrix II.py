# type: ignore
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        loop = 0
        i = 0
        j = 0

        count = 0
        while loop <= n / 2:
            while j < n - loop - 1:
                count += 1
                matrix[i][j] = count
                j += 1
            
            while i < n - loop - 1:
                count += 1
                matrix[i][j] = count
                i += 1

            while j > loop:
                count += 1
                matrix[i][j] = count
                j -= 1

            while i > loop:
                count += 1
                matrix[i][j] = count
                i -= 1

            i += 1
            j += 1
            loop += 1
        

        if n % 2 == 1:
            matrix[i - 1][j - 1] = count + 1

        return matrix
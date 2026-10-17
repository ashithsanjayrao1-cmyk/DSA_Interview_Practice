class Solution():
    def findPeak(self,matrix):
        n = len(matrix)
        m = len(matrix[0])

        max_val = -1
        max_coordinates = -1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] > max_val:
                    max_val = matrix[i][j]
                    max_coordinates = [i,j]

        return max_coordinates


s1 = Solution()
matrix = [
    [10, 20, 15],
    [21, 30, 14],
    [7, 16, 32]
]

print(s1.findPeak(matrix))
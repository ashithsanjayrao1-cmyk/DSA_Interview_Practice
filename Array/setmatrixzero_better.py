class Solution():
    def markzerobetter(self,matrix):
        n = len(matrix)
        m = len(matrix[0])


        row_track = [0] * n 
        col_track = [0] * m 

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_track[i] = 1
                    col_track[j] = 1
        for i in range(n):
            for j in range(m):
                if row_track[i] == 1 or col_track[j] == 1:
                    matrix[i][j] = 0


        return matrix
s1 = Solution()
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

s1.markzerobetter(matrix)
for row in matrix:
    print(row)
    
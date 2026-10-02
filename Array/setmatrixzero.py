class Solution():
    def setZeroes(self,matrix):
        n = len(matrix)
        m = len(matrix[0])


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = -1

                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -1


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

        return matrix

s1 = Solution()

matrix = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]


print(s1.setZeroes(matrix))
class Solution():
    def matrix(self,matrix):
        n = len(matrix)
        m = len(matrix[0])

        row_tracker = [0] * n
        col_tracker = [0] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_tracker[i] = 1
                    col_tracker[j] = 1

        for i in range(n):
            for j in range(m):
                if row_tracker[i] == 1 or col_tracker[j] == 1:
                    matrix[i][j] = 0

        return matrix
s1 = Solution()
print(s1.matrix([[1,1,1,1],[1,0,1,1],[1,1,0,1],[1,0,0,1]]))
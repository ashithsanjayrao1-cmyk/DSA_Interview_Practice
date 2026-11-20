class Solution():
    def markRow(self,matrix,n,m,i):

        for j in range(m):

            if matrix[i][j]!= 0:
                matrix[i][j] = -1

    def markCol(self,matrix,n,m,j):

        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1


    def setZeroes(self,matrix):
        n = len(matrix)
        m = len(matrix[0])


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    self.markRow(matrix,n,m,i)
                    self.markCol(matrix,n,m,j)


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0


        return matrix


s1 = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]

print(s1.setZeroes(matrix))


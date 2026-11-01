class Solution():
    def roatrateMatrix(self,matrix):
        n = len(matrix)

        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

        return matrix


s1 = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(s1.roatrateMatrix(matrix))
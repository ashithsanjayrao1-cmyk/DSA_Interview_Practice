class Solution():
    def matrix90(self,matrix):
        n = len(matrix)
        ans = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):

                ans[j][n-1-i] = matrix[i][j]


        return ans


s1 = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(s1.matrix90(matrix))


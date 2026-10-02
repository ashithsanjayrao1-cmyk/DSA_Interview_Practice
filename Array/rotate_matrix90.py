class SOlution():
    def rotatematrix(self,matrix):
        n =len(matrix)

        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    

        for i in range(n):

            matrix[i].reverse()

        return matrix
        # n = len(matrix)

        # ans = [[0 for _ in range(n)] for _ in range(n)]


        # for i in range(n):
        #     for j in range(n):
        #         ans [j][n-1-i] = matrix [i][j]

        # return ans

s1 = SOlution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = s1.rotatematrix(matrix)
for row in rotated:
    print(row)
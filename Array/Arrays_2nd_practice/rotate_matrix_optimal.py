class SOlution():
    def rotateMatrix(self,matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
        return matrix
    
s1 = SOlution()
print(s1.rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))
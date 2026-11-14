class Solution():
    def spiralMatrix(self,matrix):
        n = len(matrix)
        m = len(matrix[0])

        top = 0
        bottom = n-1
        left = 0 
        right = m-1

        sns = []

        while top<= bottom and left<=right:
            for i in range(left,right+1):
                sns.append(matrix[top][i])

            top += 1

            for i in range(top,bottom+1):
                sns.append(matrix[i][right])

            right-=1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    sns.append(matrix[bottom][i])

                bottom -=1

            if left<=right:
                for i in range(bottom,top-1,-1):
                    sns.append(matrix[i][left])

                left+=1

        return sns


s1 = Solution()
matrix = [[1,2,3,4,5,6],
          [7,8,9,10,11,12],
          [13,14,15,16,17,18],
          [19,20,21,22,23,24],
          [25,26,27,28,29,30]]

print(s1.spiralMatrix(matrix))
class Solution():
    def matrixMedian(self,matrix,n,m):


        arr = []

        for i in range(n):
            for j in range(m):
                arr.append(matrix[i][j])


        arr.sort()

        mid_index = (n*m)//2

        return arr[mid_index]


s1 = Solution()
matrix = [
    [1, 3, 6],
    [2, 6, 9],
    [3, 6, 9]
]
R = 3
C = 3

print(s1.matrixMedian(matrix,R,C))

class Solution():
    def findMax(self,matrix,n,m,col):
        max_val = -1

        index = -1

        for i in range(n):
            if matrix[i][col] > max_val:
                max_val = matrix[i][col]
                index = i

        return index


    def findPeak(self,matrix):
        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = m-1


        while low<=high:
            mid = (low+high)//2

            max_row = self.findMax(matrix,n,m,mid)

            left = matrix[max_row][mid-1] if mid-1 >= 0 else -1
            right = matrix[max_row][mid+1] if mid+1 < m else -1

            if matrix[max_row][mid] > left and matrix[max_row][mid] > right:
                return [max_row,mid]

            elif matrix[max_row][mid] < left:
                high = mid-1

            else:
                low = mid+1


        return [-1,-1]

s1 = Solution()
matrix = [
    [10, 20, 15],
    [21, 30, 14],
    [7, 16, 32]
]

print(s1.findPeak(matrix))
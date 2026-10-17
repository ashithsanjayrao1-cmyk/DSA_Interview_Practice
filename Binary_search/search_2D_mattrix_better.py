class Solution():

    def binarySearch(self,arr,target):
        n = len(arr)

        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == target:
                return True

            elif arr[mid] < target:
                low = mid+1

            else:
                high = mid-1
        return False

    def searchMatrix(self,matrix,target):
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0] <= target and target <= matrix[i][m-1]:
                return self.binarySearch(matrix[i],target)


        return False

s1 = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3

print(s1.searchMatrix(matrix,target))


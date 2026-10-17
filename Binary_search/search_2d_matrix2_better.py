class Solution():
    def binarySeach(self,arr,target):

        n = len(arr)

        low = 0 
        high = n-1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid+1

            else: 
                high = mid-1

        return -1
    


    def matrix(self,matrix,target):
        n = len(matrix)

        for i in range(n):
            ind = self.binarySeach(matrix[i],target)

            if ind != -1:
                return [i,ind]

        return [-1,-1]

s1 = Solution()

matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]

target = 14

print(s1.matrix(matrix,target))
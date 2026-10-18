class Solution():
    def upperBound(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1
        ans = n

        while low<=high:
            mid = (low+high)//2

            if arr[mid] > x:
                ans = mid
                high = mid-1

            else:
                low = mid+1


        return ans

    def blackBox(self,matrix,x):
        n = len(matrix)
        count = 0

        for i in range(n):

            count += self.upperBound(matrix[i],x)

        return count

    def median(self,matrix,n,m):
        low = min(matrix[i][0] for i in range(n))
        high = max(matrix[i][m-1] for i in range(n))

        req = (n*m)//2

        while low<=high:
            mid = (low+high)//2


            smaller_eqauls = self.blackBox(matrix,mid)

            if smaller_eqauls <= req:
                low = mid+1

            else:
                high = mid-1

        return low

s1 = Solution()
matrix = [
    [1, 3, 6],
    [2, 6, 9],
    [3, 6, 9]
]
n = 3
m = 3

print(s1.median(matrix,n,m))
    



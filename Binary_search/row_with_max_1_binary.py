class Solution():
    def lowerBound(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1
        ans = n 

        while low<=high:
            mid = (low+high)//2
            if arr[mid] >= x:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans

    def rowMatrix(self,arr,n,m):
        count_max = 0
        index = -1

        for i in range(n):
            count_ones = m-self.lowerBound(arr[i],1)

            if count_ones > count_max:
                count_max = count_ones
                index = i

        return index

s1 = Solution()
arr = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

print(s1.rowMatrix(arr,4,4))
        
class Solution():
    def lowerbound(self,arr,x):
        n = len(arr)

        low = 0
        high = n-1

        ans = n

        while low <= high:
            mid = (low+high)//2

            if arr[mid] >= x:
                ans = mid
                high = mid -1

            else:
                low = mid + 1

        return ans

s1 = Solution()
arr = [1, 2, 4, 4, 6, 8, 10]
x = 4    
xx = 5
print(s1.lowerbound(arr,xx)
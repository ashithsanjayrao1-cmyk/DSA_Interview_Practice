class Solution():
    def lowerBound(self,arr,target):

        n = len(arr)
        ans = n

        low = 0
        high = n-1

        

        while low<=high:

            mid = (low+high)//2

            if arr[mid] >= target:

                ans = mid
                high = mid-1

            else:
                low = mid+1

        return ans

s1 = Solution()

arr = [1,2,2,3]

target = 2

print(s1.lowerBound(arr,target))
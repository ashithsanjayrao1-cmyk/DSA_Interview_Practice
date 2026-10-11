class Solution():
    def findMin(self,arr):
        n= len(arr)
        low = 0
        high = n-1

        ans = float('inf')

        while low<=high:
            mid = (low+high)//2

            if arr[low] <= arr[high]:
                ans = min(ans,arr[low])

                break
            if arr[low] <= arr[mid]:
                ans = min(ans,arr[low])

                low = mid+1

            else:

                ans = min(ans,arr[mid])

                high = mid-1

        return ans

s1 = Solution()
arr = [4, 5, 6, 7, 0, 1, 2]
print(s1.findMin(arr))   
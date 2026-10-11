class Solution():
    def searchrotated(self,arr,x):

        n = len(arr)
        low =0
        high = n-1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == x:
                return mid

            if arr[low] <= arr[mid]:
                if x >= arr[low] and x <= arr[mid]:
                    high = mid-1
                else:
                    low = mid+1

            else:
                if x >= arr[mid] and x <= arr[high]:
                    low = mid+1
                else:
                    high = mid -1

        return -1

s1 = Solution()
arr = [4, 5, 6, 7, 0, 1, 2]
print(s1.searchrotated(arr, 0))
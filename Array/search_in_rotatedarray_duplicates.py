class Solution():
    def searchRptatedDuplicates(self,arr,k):
        n = len(arr)
        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == k:
                return True

            if arr[low] == arr[mid] and arr[mid] == arr[high]:
                low+=1
                high-=1

                continue

            if arr[low]<= arr[mid]:
                if k >= arr[low] and k <= arr[mid]:
                    high = mid-1

                else:
                    low = mid+1

            else:
                if k >= arr[mid] and k <= arr[high]:
                    low = mid+1
                else:
                    high = mid-1

        return False

s1 = Solution()
arr = [3, 1, 2, 3, 3, 3, 3]

print(s1.searchRptatedDuplicates(arr,2))


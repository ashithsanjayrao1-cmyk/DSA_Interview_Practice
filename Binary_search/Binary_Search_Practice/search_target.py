class Solution():
    def binarySearch(self,arr,target):
        n = len(arr)
        low = 0

        high = n-1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid-1

            else:
                low = mid+1


        return -1


s1 = Solution()
target = 9

arr = [-1,0,3,5,9,12]

print(s1.binarySearch(arr,target))



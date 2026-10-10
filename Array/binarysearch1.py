class Solution():
    def binarysearch(self,arr,target):
        n = len(arr)

        low = 0
        high = n-1

        while low <= high:

            mid = (low + high) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                high = mid - 1

            else:
                low = mid+1

        return -1


s1 = Solution()

target = 4

arr = [0,1,2,3,4,5,6,7,8,9,10]

print(s1.binarysearch(arr,target))
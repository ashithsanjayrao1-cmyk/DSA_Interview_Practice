class Solution():
    def floorCeil(self,arr,x):

        n = len(arr)

        floor = -1
        ceil = -1

        low = 0
        high = n-1

        while low<=high:

            mid = (low+high)//2

            if arr[mid] <= x:

                floor = arr[mid]

                low = mid+1

            if arr[mid] >= x:
                ceil = arr[mid]
                high = mid-1

        return floor,ceil

s1 = Solution()

x = 5

arr = [3,4,4,7,8,10]

print(s1.floorCeil(arr,x))
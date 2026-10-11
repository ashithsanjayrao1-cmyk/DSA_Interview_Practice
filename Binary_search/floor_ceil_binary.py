class Solution():
    def floorCiel(self,arr,x):

        n = len(arr)

        low = 0

        high = n-1

        floor_val = -1

        ceil_val = -1

        while low<= high:
            mid = (low+high)//2

            if arr[mid]<=x:
                floor_val = arr[mid]

                low = mid+1
            elif arr[mid]>=x:
                ceil_val = arr[mid]
                high = mid-1
        return floor_val,ceil_val
                
s1 = Solution()
arr = [3, 4, 4, 7, 8, 10]
x = 5

print(s1.floorCiel(arr,x))

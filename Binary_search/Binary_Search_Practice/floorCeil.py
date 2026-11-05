class Solution():
    def floorCeil(self,arr,x):

        n = len(arr)
        low = 0
        high = n-1


        while low<=high:
            mid = (low+high)//2

            if arr[mid] <= x:
                low = mid+1

            if arr[mid] >= x:
                high = mid-1

        return arr[high],arr[low]


s1 = Solution()
arr = [3,4,4,7,8,10]
print(s1.floorCeil(arr,5))
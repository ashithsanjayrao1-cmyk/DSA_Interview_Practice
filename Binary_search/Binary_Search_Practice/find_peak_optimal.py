class Solution():
    def findPeak(self,arr):
        n = len(arr)

        if n == 1:
            return arr[0]
        
        
        if arr[0] > arr[1]:
            return arr[0]

        if arr[n-1] > arr[n-2]:
            return arr[n-1]

        low = 1
        high = n-2

        while low <= high:
            mid = (low+high)//2

            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return arr[mid]

            elif arr[mid] > arr[mid-1]:
                low = mid+1

            elif arr[mid] > arr[mid+1]:
                high = mid-1

            else:  
                low = mid+1
        return -1
s1 = Solution()

print(s1.findPeak([-2, -1, 3, 4, 5]))
class Solution():
    def firstOccurance(self,arr,x):
        n = len(arr)

        low = 0
        high = n-1
        first = -1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == x:
                first = mid
                high = mid-1
            elif arr[mid]<x:
                low = mid+1

            else:
                high = mid -1

        return first

    def lastOccurance(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1
        last = -1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] == x:
                last = mid
                low = mid+1
            elif arr[mid]<x:
                low = mid+1

            else:
                high = mid-1

        return last
    def search(self,arr,x):
        first = self.firstOccurance(arr,x)

        if first == -1:
            return[-1,-1]

        last = self.lastOccurance(arr,x)

        return [first,last]

s1 = Solution()
arr = [2, 4, 6, 8, 8, 8, 11, 13]

print(s1.search(arr,8))
    
            
class Solution:
    def first(self,arr,x):
        n = len(arr)

        low = 0
        high = n-1
        first = -1

        while low<=high:
            mid = (low+high)//2
            if arr[mid] == x:
                first = mid
                high = mid-1
            elif arr[mid] < x:
                low = mid+1
            else:
                high = mid-1
        return first

    def last(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1
        last = -1

        while low<=high:
            mid = (low+high)//2
            if arr[mid] == x:
                last = mid
                low = mid+1
            elif arr[mid] < x:
                low = mid+1
            else:
                high = mid-1

        return last


    def countOccurrences(self, arr, target):
        first = self.first(arr,target)

        if first == -1:
            return 0

        last = self.last(arr,target)

        return last-first+1

s1 = Solution()

arr = [0,1,1,1,1,1,2,3,4,5,6]

print(s1.countOccurrences(arr,1))

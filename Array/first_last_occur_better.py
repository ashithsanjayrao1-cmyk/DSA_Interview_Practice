class Solution():
    def lowerbound(self,arr,x):

        n = len(arr)
        low = 0
        ans = n
        high = n-1

        while low<=high:
            mid = (low+high)//2
            if arr[mid] >= x:
                ans = mid
                high = mid-1

            else:
                low = mid+1
        return ans

    def upperbound(self,arr,x):

        n = len(arr)
        low = 0
        high = n-1
        ans = n

        while low <= high:
            mid = (low+high)//2

            if arr[mid] > x:
                ans = mid
                high = mid-1

            else:
                low = mid+1

        return ans

    def firstlast(self,arr,x):
        n = len(arr)

        lb = self.lowerbound(arr,x)

        if lb == n or arr[lb]!=x:
            return[-1,-1]

        ub= self.upperbound(arr,x)

        return [lb,ub-1]

s1 = Solution()

arr = [2, 4, 6, 8, 8, 8, 11, 13]

print(s1.firstlast(arr,8))

print(s1.firstlast(arr,10))
                



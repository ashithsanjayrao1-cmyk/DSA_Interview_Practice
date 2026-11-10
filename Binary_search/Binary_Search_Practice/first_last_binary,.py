class Solution():
    def First(self,arr,x):
        n = len(arr)
        low = 0
        high = n-1
        ans = n

        while low <= high:
            mid = (low+high)//2

            if arr[mid] >= x:
                ans = mid
                high = mid-1

            else:

                low = mid+1

        return ans

    def Last(self,arr,x):
        n = len(arr)
        low = 0 
        high = n-1
        ans = n

        while low<=high:
            mid = (low+high)//2

            if arr[mid] > x:
                ans = mid
                high = mid-1

            else:

                low = mid+1

        return ans

    def FirstLast(self,arr,x):
        n = len(arr)

        lb = self.First(arr,x)

        if lb == n or arr[lb] != x:
            return [-1,-1]
        up = self.Last(arr,x)

        return lb,up-1

s1 = Solution()


arr = [2,4,6,8,8,8,11,13]

print(s1.FirstLast(arr,8))

        




    

    
import math
class Solution():


    def func(self,arr,h):
        n = len(arr)
        total_hours = 0

        for i in range(n):
            total_hours += math.ceil(arr[i]/h)
        return total_hours


    def koko_optimal(self,arr,h):

        low = 0
        high = max(arr)
        ans = -1

        while low<=high:
            mid = (low+high)//2 

            total_hours = self.func(arr,mid)

            if total_hours <= h:
                ans = mid

                high = mid-1

            else:
                low = mid+1

        return low

s1 = Solution()
arr = [7,15,6,3]

h = 8

print(s1.koko_optimal(arr,h))
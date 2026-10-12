import math


class Solution():

    def calculations(self,arr,hourly):
        n = len(arr)

        total_hours = 0

        for i in range(n):
            total_hours += math.ceil(arr[i]/hourly)

        return total_hours
    
        
    def kokoEating(self,arr,h):

        low = 1
        high = max(arr)  
        ans = float('inf')

        while low<=high:
            mid = (low+high)//2
            total_hours = self.calculations(arr,mid)
            if total_hours <= h:
                ans = mid

                high = mid-1

            else:
                low = mid+1

        return ans

s1= Solution()
arr = [7,15,6,3]
h = 8

print(s1.kokoEating(arr,h))


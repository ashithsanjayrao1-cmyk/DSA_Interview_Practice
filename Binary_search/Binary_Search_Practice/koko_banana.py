
import math
class Solution():
    def func(self,arr,hourly):

        n = len(arr)

        total_hours = 1

        for i in range(n-1):

            total_hours += math.ceil(arr[i]/hourly)

        return total_hours


    def koko(self,arr,h):
        n = max(arr)

        for i in range(1,n+1):

            req_time = self.func(arr,i) 

            if req_time <= h:
                return i

        return -1
s1 = Solution()
arr = [7,15,6,3]
h = 8
print(s1.koko(arr,h))
        


    
            



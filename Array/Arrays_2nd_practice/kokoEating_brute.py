import math
class Solution():

    def func(self,arr,hourly):

        n = len(arr)

        total_hours = 0

        for i in range(n):
         

            total_hours+=math.ceil(arr[i]/hourly)
        return total_hours

    def koko(self,arr,h):

        for i in range(1,max(arr)+1):

            reqtimw = self.func(arr,i)

            if reqtimw <= h:
                return i

s1 = Solution()

print(s1.koko([3,7,6,11],8))

        

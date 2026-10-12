import math
class Solution():

    def calculation(self,arr,hourly):
        n = len(arr)
        total_hours = 0

        for i in range(n):

            total_hours += math.ceil(arr[i]/hourly)

        return total_hours
    

    def koko(self,arr,h):

        n = max(arr)

        for i in range(1,n):
            req_time = self.calculation(arr,i)
            if req_time <= h:
                return i

s1 = Solution()

s1= Solution()
arr = [25, 12, 8, 14, 19]
h = 5

print(s1.koko(arr,h))




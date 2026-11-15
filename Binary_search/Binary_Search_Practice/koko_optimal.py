import math
class Solution():
    def func(self,arr,hourly):
        n = len(arr)

        total_hours = 0

        for i in range(n-1):

            total_hours += math.ceil(arr[i]/hourly)
        return total_hours

    def koko(self,arr,h):
        low = 0
        high = max(arr)


        while low<=high:
            mid = (low+high)//2

            if self.func(arr,mid) <= h:

                high = mid-1
            else:
                low = mid+1
        return low
s1 =Solution()
print(s1.koko([7,15,6,3],8)) 
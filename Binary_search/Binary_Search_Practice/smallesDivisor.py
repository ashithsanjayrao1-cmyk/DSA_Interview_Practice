import math
class Solution():
    def calculate(self,arr,divisor):
        total = 0

        for i in range(len(arr)):

            total += math.ceil(arr[i]/divisor)

        return total

    def binarySearch(self,arr,threshold):

        low = 1
        high = max(arr)
        ans = -1

        while low <= high:
            mid = (low+high)//2

            if self.calculate(arr,mid) <= threshold:

                ans = mid

                high = mid-1

            else:
                low = mid+1

        return low

s1 = Solution()

arr = [1,2,3,4,5]

threshold = 8

print(s1.binarySearch(arr,threshold))

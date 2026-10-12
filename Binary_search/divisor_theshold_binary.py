import math
class Soluton():
    def calculateSum(self,arr,d):
        total = 0 
        for i in arr:
            total += math.ceil(i/d)
        return total

    def smalleDivisor(self,arr,threshold):
        low = 1
        high = max(arr)
        ans = -1 
        while low<=high:
            mid = (low+high)//2

            if self.calculateSum(arr,mid)<=threshold:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans


s1 = Soluton()

arr =[1,2,5,9]
threshold = 6


print(s1.smalleDivisor(arr,threshold))
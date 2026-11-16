class Solution():
    def func(self,weight,capacity):
        n = len(weight)
        count = 0

        day = 1

        for i in range(n):
            if count+weight[i] > capacity:
                day+=1

                count = weight[i]
            else:

                count += weight[i]

        return day
    def binarySeacrh(self,weight,days):

        low = max(weight)
        high = sum(weight)

        while low <= high:
            mid = (low+high)//2

            req_days = self.func(weight,mid) 

            if req_days <= days:
                high = mid-1
            else:
                low = mid+1



        return low      

s1 = Solution()

print(s1.binarySeacrh([3,2,2,4,1,4],3))
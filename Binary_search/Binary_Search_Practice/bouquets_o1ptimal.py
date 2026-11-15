class Solution():

    def func(self,bloomday,day,m,k):
        n = len(bloomday)

        count = 0
        bouquets = 0

        for i in range(n):
            if bloomday[i]<=day:
                count+=1
            else:
                bouquets += (count//k)
                count = 0
        bouquets += (count//k)
        if bouquets >=m:
            return True
        else:
            return False

        
    def bouquets(self,bloomday,m,k):

        n = len(bloomday)

        if m*k > n:
            return -1

        low = min(bloomday)
        high  = max(bloomday)

        while low<=high:
            mid = (low+high)//2

            possible = self.func(bloomday,mid,m,k)
            

            if possible == True:
                high = mid-1
            else:
                low = mid+1
        return low
s1 = Solution()

print(s1.bouquets([7,7,7,7,13,11,12,7],2,3))
class Solution():
    def possible(self,arr,days,m,k):
        count = 0

        bouquets = 0

        n = len(arr)


        for i in range(n):

            if arr[i] <= days:
                count+=1

            else:

                bouquets += (count//k)
                count = 0

        bouquets += (count//k)
        return bouquets >= m


    def minDays(self,days,m,k):

        n = len(days)

        if m*k > n:
            return -1

        min_day = min(days)
        max_day = max(days)

        for day in range(min_day,max_day+1):

            if self.possible(days,day,m,k):
                return day

        return -1

s1 = Solution()
arr = [7,7,7,7,13,11,12,7]

print(s1.minDays(arr,2,3))
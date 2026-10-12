class Solution():
    def possible(self,bloomDay,day,m,k):
        count = 0
        bouquets = 0

        for bloom in bloomDay:
            if bloom <= day:
                count+=1

            else:
                bouquets += (count//k)
                count = 0

        bouquets += (count//k)
        return bouquets >= m

    def minDays(self,bloomDay,m,k):
        n = len(bloomDay)

        if m*k > n:
            return -1

        min_day = min(bloomDay)
        max_day = max(bloomDay)

        for day in range(min_day,max_day+1):
            if self.possible(bloomDay,day,m,k):
                return day

        return -1

s1 = Solution()
bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

print(s1.minDays(bloomDay,m,k))

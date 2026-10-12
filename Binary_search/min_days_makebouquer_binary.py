class Solution():
    def possible(self,bloomDay,dday,m,k):
        bouquets = 0
        count = 0


        for bloom in bloomDay:
            if bloom <= dday:
                count+=1
            else:
                bouquets += (count//k) 
                count = 0

        bouquets += (count//k)
        return bouquets >= m

    def binarysearch(self,arr,m,k):

        n =len(arr)
        if n<m*k:
            return -1
        
        low = min(arr)
        high = max(arr)
        ans = -1

        while low <= high:
            mid = (low+high)//2

            if self.possible(arr,mid,m,k):
                ans = mid
                high = mid-1
            else:
                low = mid +1

        return ans

s1 = Solution()
bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3

print(s1.binarysearch(bloomDay,m,k))

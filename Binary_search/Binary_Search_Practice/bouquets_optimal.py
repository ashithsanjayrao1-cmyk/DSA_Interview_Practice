class Solution():
    def possible(self,bloomdays,day,m,k):
        count = 0
        bouquets = 0

        for bloom in bloomdays:
            if bloom <= day:
                count +=1

            else:
                bouquets += (count //k)
                count = 0

        bouquets  += (count//k)
        return bouquets >= m

    def binary(self,arr,m,k):
        n = len(arr)

        if n < m*k:
            return -1

        low = min(arr)
        high = max(arr)

        while low<=high:
            mid =(low+high)//2

            if self.possible(arr,mid,m,k):

                high = mid-1

            else:
                low = mid+1
        return low
s1 = Solution()
arr = [7,7,7,7,13,11,12,7]

print(s1.binary(arr,2,3))
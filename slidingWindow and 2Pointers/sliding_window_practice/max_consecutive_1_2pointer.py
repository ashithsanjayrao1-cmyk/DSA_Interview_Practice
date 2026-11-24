class Solution():
    def max_consecutive1(self,arr,k):
        n = len(arr)
        l = 0
        r = 0
        max_len = 0

        zeroes = 0


        while r < n:
            if arr[r] == 0:
                zeroes += 1

            if zeroes > k:
                if arr[l] == 0:
                    zeroes -=1
                l += 1

            if zeroes <= k:
                length = r-l+1
                max_len = max(max_len,length)

            r+=1
            

        return max_len
s1 = Solution()
print(s1.max_consecutive1([1,1,1,0,0,0,1,1,1,1,0],2))
        
                    
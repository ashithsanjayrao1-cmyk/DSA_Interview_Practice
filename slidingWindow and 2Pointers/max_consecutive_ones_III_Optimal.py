class Solution():
    def maxOnes(self,arr: list,k : int) -> int:

        max_len = 0

        n = len(arr)
        l = 0
        r = 0
        zeroes = 0

        while r<n:
            if arr[r] == 0:
                zeroes+=1

            if zeroes > k:
                if arr[l] == 0:
                    zeroes -=1
                l+=1

            if zeroes <= k:
                length = r-l+1
                max_len = max(length,max_len)

            r+=1

        return max_len

s1 = Solution()

arr = [1,1,1,0,0,0,1,1,1,1,0]

k = 2

print(s1.maxOnes(arr,k))
    
class Solution():
    def assignCookies(self,greed,size):

        greed.sort()
        size.sort()
        n = len(greed)
        m = len(size)

        l = 0
        r = 0

        while l<m and r<n:

            if greed[r] <= size[l]:
                r+=1

            l+=1

        return r
    
s1 = Solution()
print(s1.assignCookies([1,5,3,3,4],[4,2,1,2,1,3]))


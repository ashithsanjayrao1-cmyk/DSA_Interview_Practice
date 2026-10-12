class Solution():
    def linearsearch(self,n):
        ans =1

        for i in range(1,n+1):
            if i*i <= n:
                ans = i
            else:
                break

        return ans
    
s1 = Solution()
n = 25

print(s1.linearsearch(n))
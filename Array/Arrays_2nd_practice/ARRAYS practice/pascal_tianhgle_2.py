class Solution():
    def nCr(self,n,r):
        res = 1

        for i in range(r):

            res = res * (n-i)
            res = res // (i+1)

        return res

    def printRow(self,n):
        ans = []

        for i in range(1,n+1):
            ans.append(self.nCr(n-1,i-1))


        return ans



s1 = Solution()

print(s1.printRow(3))
class Solution():
    def pascalTriangle1(self,n,r):

        res = 1

        for i in range(r):

            res = res*(n-i)
            res = res // (i+1)

        return res

    def pascal(self,row,col):
        return self.pascalTriangle1(row-1,col-1)
s1 = Solution()
print(s1.pascal(6,3))
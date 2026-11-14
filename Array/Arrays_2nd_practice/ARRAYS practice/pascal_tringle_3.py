class Solution():
    def pascalTriangle(self,row):
        ans = 1

        ansRow = [1]

        for i in range(1,row):
            ans = ans*(row-i)
            ans = ans//(i)
            ansRow.append(ans)

        return ansRow



    def Triganle(self,n):

        ans = []

        for i in range(1,n+1):
            ans.append(self.pascalTriangle(i))

        return ans


s1 = Solution()

print(s1.pascalTriangle(6))
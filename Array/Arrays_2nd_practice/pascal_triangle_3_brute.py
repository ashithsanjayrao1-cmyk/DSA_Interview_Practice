class Solution():
    def pascalTriangle(self,n,r):
        res = 1

        for i in range(r):

            res = res*(n-i)
            res = res //(i+1)

        return res

    def generateTriangle(self,n):
        ans = []

        for i in range(1,n+1):
            temp_list = []

            for j in range(1,i+1):
                temp_list.append(self.pascalTriangle(i-1,j-1))

            ans.append(temp_list)

        return ans
s1 = Solution()
print(s1.generateTriangle(16))



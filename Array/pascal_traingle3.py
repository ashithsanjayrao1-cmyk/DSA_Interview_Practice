class Solution():

    def generateRow(self,row):
        ans_val = 1
        ansrow = [1]

        for col in range(1,row):

            ans_val = ans_val * (row - col)
            ans_val = ans_val // col
            ansrow.append(ans_val)

        return ansrow


    def generateTriangle(self,n):
        ans = []
        for row in range(1, n+1):
            ans.append(self.generateRow(row))

        return ans
    # def nCr(self,n,r):
    #     res = 1

    #     for i in range(r):
    #         res = res * (n-i)
    #         res = res // (i+1)

    #     return res


    # def generatetriangle(self,n):
    #     ans = []

    #     for row in range(1,n+1):
    #         temp_list = []

    #         for col in range(1, row + 1):
    #             temp_list.append(self.nCr(row-1,col-1))


    #         ans.append(temp_list)

    #     return ans

s1 = Solution()

print(s1.generateTriangle(6))
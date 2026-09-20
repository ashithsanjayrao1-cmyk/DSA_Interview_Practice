class Solution():
    def pattern5(self,n):
        for i in range(1,n+1):
            for j in range(i,n+1):
                print("*",end = " ")

            print()


s1 = Solution()

n = 5

s1.pattern5(n)
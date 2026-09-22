class Solution:
    def pattern7(self,n):

        for i in range(1,n+1):
            for j in range(n-i):
                print(" ",end = "")
            for k in range(2*i-1):     
                print("*",end="")   

            print()

            

s1 = Solution()

n = 5

s1.pattern7(n)
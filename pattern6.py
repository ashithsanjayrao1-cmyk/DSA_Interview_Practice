class Solution():

    def pattern6(self,n):
        for i in range(1,n+1):
            for j in range(1,n-i+2):
                print(j,end =" ")

            print()



s1 = Solution()

n = 5

s1.pattern6(n)
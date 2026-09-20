class Solution():
    def pattern4(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end=" ")

            print()


s1 = Solution()

n = 5

s1.pattern4(n)
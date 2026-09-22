class Solution():

    def pattern13(self,n):
        num = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(num,end=" ")
                num = num+1

            print()



s1 = Solution()

n = 5

s1.pattern13(n)
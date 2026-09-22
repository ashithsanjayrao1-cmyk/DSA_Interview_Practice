class Solution():
    def pattern10(self,n):
        for i in range(1,2*n):

                if i <=  n:
                    stars = i

                else:
                    stars = 2 * n -i

                for j in range(stars):
                     print("*",end="")

                print()




s1 = Solution()

n=5

s1.pattern10(n)
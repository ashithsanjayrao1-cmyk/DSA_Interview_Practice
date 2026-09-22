class Solution():
    def pattern12(self,n):

        spaces = 2 * (n-1)
        for i in range(1,n+1):
            for j in range(1,i+1):

                print(j,end="")


            for j in range(spaces):
                print(" ",end="")


            for j in range(i,0, -1):
                print(j,end = "")



            print()
            spaces -= 2


s1 = Solution()
n = 4
s1.pattern12(n)
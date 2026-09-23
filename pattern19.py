class Solution():
    def pattern18(self,n):

        spaces = 0

        for i in range(n):
            for j in range(n-i):
                print("*",end="")

            for j in range(spaces): 

                print(" ",end="")
                
                
                


            for j in range(n-i):
                print("*",end="")

            print()
            spaces += 2


        spaces = 2*n-8


        for i in range(n):
            for j in range(i,n+1):

                print("*",end="")

            for j in range(spaces): 

                print(" ",end="")
                
                
                
            for j in range(n-i):
                print("*",end="")

            print()

            
            
            




            
            


                


s1 = Solution()
n = 5
s1.pattern18(n)
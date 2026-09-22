class Solution():
    def pattern17(self,n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")


            
            ch = ord('A')

            breakpoint = (2*i+1)//2


            for j in range(1,2*i+2):
                print(chr(ch),end="")

                if j<= breakpoint:
                    ch+=1

                else:
                    ch -= 1 


            for j in range(n-i-1):
                print(" ",end="")

            print()
 

s1 = Solution()

n = 5

s1.pattern17(n)
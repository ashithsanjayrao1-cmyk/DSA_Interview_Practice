class Solution():

    def pattern14(self,n):
        for i in range(1,n+1):
            for j in range(i):

                letter = chr(ord('A')+j)
                print(letter,end="")
                

            print()


s1 = Solution()

n = 5

s1.pattern14(n)

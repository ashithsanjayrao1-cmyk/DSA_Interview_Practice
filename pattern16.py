class Solution():
    def pattern16(self,n):
        for i in range(n+1):
            for j in range(i+1):
                letter = chr(ord('A')+i)
                print(letter,end="")


            print()


s1 = Solution()

n = 5

s1.pattern16(n)
class Solution():
    def pattern15(self,n):
        for i in range(n+1):
            for j in range(n-i):
                letter = chr(ord('A')+ j)

                print(letter,end=" ")

            print()


s1 = Solution()

n = 5

s1.pattern15(n)
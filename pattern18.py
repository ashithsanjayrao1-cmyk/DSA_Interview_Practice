class Solution():
    def pattern18(self,n):
        for i in range(1,n+1):
            start_val = ord('A') + n - i 
            
            # 2. Print 'i' number of characters
            for j in range(i):
                # Add 'j' to the starting value to count up (E -> F, D -> E)
                letter = chr(start_val + j)
                print(letter, end=" ")
                
            print()

s1 = Solution()
n = 5
s1.pattern18(n)




            


class SOlution():
    def sqrt(self,n):

        ans = 1

        for i in range(1,n+1):
            if  i*i <= n:
                ans = i 
            else:
                break

        return ans


s1 = SOlution()

print(s1.sqrt(25))
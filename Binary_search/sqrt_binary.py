class SOlution():
    def sqrtbinary(self,n):
        ans = 1
        low = 1
        high = n
        while(low<=high):
            mid = (low+high)//2

            if mid*mid <=n:
                ans = mid
                low = mid+1
            else: 
                high = mid-1

        return ans

s1 = SOlution()

n = 25

print(s1.sqrtbinary(n))
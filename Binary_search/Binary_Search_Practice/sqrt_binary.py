class SOlution():
    def binarysearcg(self,n):
        ans = 1
        low = 1
        high = n

        while low<=high:
            mid = (low+high)//2

            if mid*mid == n:
                ans = mid
                return mid

            if mid*mid < n:
                ans = mid
                low = mid+1

            else:
                high = mid-1


        return ans

s1 = SOlution()

n = 28

print(s1.binarysearcg(n))

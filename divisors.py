class Solution():
    def divisors(self,n):

        for i in range(1,n+1):
            if n % i == 0:
                print(i)

s1 = Solution()

n = 36

s1.divisors(n)
            
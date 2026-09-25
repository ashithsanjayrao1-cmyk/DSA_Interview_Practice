class Solution():
    def prime(self,n):
        count = 0

        for i in range(1,n+1):
            if(n%i == 0):
                count += 1

        if count == 2:
            print("Its is prime number")

        else:
            print("It is not a prime number")

        return count


s1 = Solution()

n = 3

s1.prime(n)

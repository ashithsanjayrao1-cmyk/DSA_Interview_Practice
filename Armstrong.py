class Solution():
    def armstrong(self,n):
        sum = 0

        dup_n = n


        while(n>0):
            lastdigit = n % 10

            sum = sum + (lastdigit*lastdigit*lastdigit)

            n = n//10

        if sum == dup_n:
            print("Its an armstrong number")

        else:
            print("Its not an armstrong number")

        return sum



s1 = Solution()

n = 1531

s1.armstrong(n)
class Solution():
    def palindrome(self,n):

        origin_n = n
        rev_num = 0

        while n > 0:

            lastdigit = n % 10
            rev_num = (rev_num * 10) + lastdigit

            n = n //10

        if rev_num == origin_n:
            print("Then given number is palindrome")

        else:
            print("The given number is not a palindrome")


        return rev_num
                


s1 = Solution()


n = 131

s1.palindrome(n)
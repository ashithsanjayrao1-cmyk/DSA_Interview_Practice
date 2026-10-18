class Solution():
    def myAtoi(self,s:str) -> int:
        n = len(s)
        i = 0

        while i<n and s[i] == ' ':
            i+=1

        if i==n:
            return 0


        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1

        elif s[i] == '+':
            i+=1

        result = 0

        while i<n and s[i].isdigit():
            digit = int(s[i])

            result = (result*10) + digit

            i+=1

        result = result * sign

        INT_MAX = (2**31)-1
        INT_MIN = -(2**31)

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN

        return result

s1 = Solution()
print(s1.myAtoi("   -123abc45")) 




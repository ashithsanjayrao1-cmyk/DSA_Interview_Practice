class Solution():
    def gcd_hcf(self,a,b):


        while a > 0 and b>0:

            if a>b:
                a = a % b

            else:
                b = b % a

        if a == 0:
            return b
        else:
            return a


s1 = Solution()

print(s1.gcd_hcf(9,12))

print(s1.gcd_hcf(20,15))

                
            
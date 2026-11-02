class Solution()
    def myPow(self,x:float,n:int) -> float:

        m = n
        nn = abs(n)

        ans = 1.0

        while nn > 0:
            if nn % 2 == 1:

                ans = ans * x
                nn = nn-1

            else:
                x = x * x
                nn = nn //2

        if m<0:
            ans = 1.0/ans

        return ans
    
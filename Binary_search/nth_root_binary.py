class Solution():
    def multiply(self,mid,n,m):
        ans = 1

        for i in range(1,n+1):
            ans = ans  * mid

            if ans > m:
                return 2

        if ans == m:
            return 1

        return 0

    def NthROot(self,n,m):
        low = 1
        high = m

        while low<=high:
            mid = (low+high)//2

            val = self.multiply(mid,n,m)

            if val == 1:
                return mid

            elif val == 0:
                low = mid+1
            else:
                high = mid-1


        return -1


s1= Solution()

print(s1.NthROot(4,15))
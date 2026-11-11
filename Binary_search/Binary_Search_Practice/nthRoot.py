class Solution():
    def nthRoot(self,n,m):
        low = 0
        high = m

        ans = 1

        while low<=high:
            mid = (low+high)//2

            if mid*n <= m:
                ans = mid
                low = mid+1

            else:

                high = mid-1

        return ans

s1 = Solution()

print(s1.nthRoot(3,27))

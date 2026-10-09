class Solution():
    def maxproduct(self,arr):
        n = len(arr)

        max_prod = float('-inf')

        pref = 1

        suff = 1

        for i in range(n):
            if pref == 0:
                pref = 1

            if suff == 0:
                pref = 1

            pref *= arr[i]

            suff *= arr[n-i-1]

            max_prod = max(max_prod,max(pref,suff))

        return max_prod

s1 = Solution()
arr = [2, 3, -2, 4]
print(s1.maxproduct(arr))
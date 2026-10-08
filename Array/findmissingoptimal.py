class Solution():
    def findmissingmath(self,arr):
        n = len(arr)

        SN = (n*(n+1)) // 2

        S2N = (n * (n+1) *(2*n+1)) // 6

        S = 0
        S2 = 0

        for num in arr:
            S += num
            S2 += num * num

        val1 = S - SN
        val2 = S2 - S2N

        val2 = val2 // val1

        repeating = (val1 + val2) // 2

        missing = repeating - val1

        return[repeating,missing]


s1 = Solution()
arr = [3, 1, 2, 5, 3]
print(s1.findmissingmath(arr))      
class Solution:
    def missing(self,arr):
        n = len(arr)

        expected = n*(n+1)//2

        actual = 0

        for i in range(n):
            actual += arr[i]

        return expected - actual
s1 = Solution()
arr = [1,2,3,4,5,7]
print(s1.missing(arr))
    
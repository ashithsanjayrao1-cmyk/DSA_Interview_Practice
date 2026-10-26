class Solution():
    def missinNumber(self,arr):

        n = len(arr)+1
        expected = n*(n+1)//2

        actual = 0

        for i in range(len(arr)):
            actual += arr[i]

        return expected - actual


s1 = Solution()
arr = [1,2,3,5]

print(s1.missinNumber(arr))
class Solution():
    def missing(self,arr):
        n = len(arr)
        hash = [0]*(n+1)

        for i in range(n):
            hash[arr[i]] = 1

        for i in range(1,n+1):
            if hash[i] == 0:
                return i

        return -1

s1 = Solution()
print(s1.missing([0,1,2,3,4]))
class Solution():
    def missingNumber(self,arr):
        n = len(arr)+1
        hash_map = [0] * (n+1)

        for i in range(n-1):
            hash_map[arr[i]] = 1

        for i in range(1,n):
            if hash_map[i] == 0:
                return i


s1 = Solution()
arr = [1,2,3,5]

print(s1.missingNumber(arr))
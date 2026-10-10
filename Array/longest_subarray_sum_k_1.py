class Solution():
    def longestSubarryWithSumK(self,arr,k):

        n = len(arr)

        long = 0

        for i in range(n):
            sum = 0
            for j in range(i,n):

                sum += arr[j]
                
                if sum == k:
                    long = max(long,j-i+1)

        return long

s1 = Solution()
arr = [1, 2, 3, 1, 1, 1, 1]
k =3

print(s1.longestSubarryWithSumK(arr,k))
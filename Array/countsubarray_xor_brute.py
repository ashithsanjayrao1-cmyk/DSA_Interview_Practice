class Solution():
    def subarraysXOR(self,arr,k):

        n = len(arr)

        count = 0

        for i in range(n):
            for j in range(i,n):

                xor = 0

                for m in range(i,j+1):

                    xor ^= arr[m]

                if xor == k:
                    count += 1

        return count

    
s1 = Solution()
arr = [4, 2, 2, 6, 4]
k = 6

print(s1.subarraysXOR(arr,k))

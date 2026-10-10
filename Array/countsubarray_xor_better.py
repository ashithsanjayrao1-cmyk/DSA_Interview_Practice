class Solution():
    def countsubarray(self,arr,k):

        n = len(arr)

        count = 0

        for i in range(n):
            xor = 0

            for j in range(i,n):
                xor ^= arr[j]


                if xor == k:
                    count += 1

        return count
    

s1 = Solution()

arr = [4, 2, 2, 6, 4]
k = 6


print(s1.countsubarray(arr,k))


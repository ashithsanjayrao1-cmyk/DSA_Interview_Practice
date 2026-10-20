class Solution():
    def maxOnes(self,arr,k):
        n = len(arr)
        max_len = 0
        for i in range(n):

            zeroes = 0

            for j in range(i,n):

                if arr[j] == 0:
                    zeroes +=1

                if zeroes <= k:
                    length = j-i+1
                    max_len = max(max_len,length)

                else:
                    break


        return max_len


s1 = Solution()

arr = [1,1,1,0,0,0,1,1,1,1,0]

k = 2

print(s1.maxOnes(arr,k))
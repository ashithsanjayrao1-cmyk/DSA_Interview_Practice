class Solution():
    def findKthNumber(self,arr,k):

        for num in arr:
            if num <= k:
                k += 1
            else:
                break

        return k

s1 = Solution()
arr = [2, 3, 4, 7, 11]
k = 5

print(s1.findKthNumber(arr,k))
                


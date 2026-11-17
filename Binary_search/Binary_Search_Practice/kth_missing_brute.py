class Solution():
    def kthMissing(self,arr,k):

        n = len(arr)

        for i in range(n):

            
            
            if arr[i] <= k:
                k+=1
            else:
                break

        return k

s1 = Solution()
print(s1.kthMissing([1,4,6,8,9],3))
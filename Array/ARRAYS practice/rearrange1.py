class Solution():
    def rearrange(self,arr):
        n = len(arr)

        pos = 0
        neg = 1

        ans = [0] * n


        for i in range(n):
            if arr[i] > 0:
                ans[pos] = arr[i]
                pos += 2

            else:
                ans[neg] = arr[i]
                neg += 2

        return ans
    


s1 = Solution()

arr = [2,4,5,-1,-3,-4]

print(s1.rearrange(arr))
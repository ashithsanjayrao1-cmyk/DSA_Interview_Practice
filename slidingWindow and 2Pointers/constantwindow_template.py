class Solution():
    def maxSubArray(self,arr,k):
        n = len(arr)

        if n < k:
            return -1

        current_sum = sum(arr[:k])

        max_sum = current_sum

        l = 0
        r = k-1

        while r < n-1:
            current_sum = current_sum - arr[l]
            l+=1

            r+=1

            current_sum = current_sum+arr[r]

            max_sum = max(current_sum,max_sum)

  
        return max_sum

s1 = Solution()
arr = [-1, 2, 3, 3, 4, 5, -1]
k = 4

print(s1.maxSubArray(arr,k))
    
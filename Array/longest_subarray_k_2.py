class Solution():
    def longestSubarrayWithSumKBetter(self,arr,k):
        n = len(arr)
        prefix_sum_map = {}
        max_len = 0
        running_sum = 0

        for i in range(n):
            running_sum += arr[i]

            if running_sum == k:
                max_len = max(max_len,i+1)

            rem = running_sum - k


            if rem in prefix_sum_map:
                length = i-prefix_sum_map[rem]
                max_len = max(max_len,length)


            if running_sum not in prefix_sum_map:
                prefix_sum_map[running_sum] = i

        return max_len

s1 = Solution()
arr = [2, 0, 0, 3]
k = 3

print(s1.longestSubarrayWithSumKBetter(arr,k))

class Solution():
    def kadanesAlgorithm(self,arr):
        n = len(arr)
        current_sum = 0
        max_sum = float('-inf')

        for i in range(n):
            current_sum += arr[i]

            if current_sum > max_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        return max_sum
s1 = Solution()
print(s1.kadanesAlgorithm([-2,-3,4,-1,-2,1,5,-3]))


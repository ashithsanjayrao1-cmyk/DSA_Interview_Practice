import sys
class Solution:
    def maxsubarray(self,arr):

        max_sum = -sys.maxsize-1

        current_sum = 0

        for i in range(len(arr)):
            current_sum += arr[i]

            if current_sum > max_sum:
                max_sum = current_sum


            if current_sum < 0:
                current_sum = 0 

        return max_sum


s1 = Solution()

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s1.maxsubarray(arr))
class Solution():
    def MaxSum(self,arr):
        n = len(arr)
        max_sum = 0

        for i in range(n):
            current_sum = 0

            for j in range(i,n):

                current_sum += arr[j]

                max_sum = max(max_sum,current_sum)

        return max_sum
s1 = Solution()
print(s1.MaxSum([2,3,5,-2,7,-4]))
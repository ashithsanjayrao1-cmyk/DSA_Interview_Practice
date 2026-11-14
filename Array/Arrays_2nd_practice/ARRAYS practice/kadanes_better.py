class Solution():
    def kadanesBetter(self,arr):
        n = len(arr)
        max_sum = float("-inf")

        for i in range(n):
            sum = 0
            for j in range(i,n):

                sum += arr[j]

                max_sum = max(max_sum,sum)

        return max_sum



s1 = Solution()

arr = [2,3,5,-2,7,-4]

print(s1.kadanesBetter(arr))
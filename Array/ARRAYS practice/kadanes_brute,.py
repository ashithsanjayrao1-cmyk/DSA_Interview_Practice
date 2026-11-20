class Solution():
    def kadanesBrute(self,arr):
        n = len(arr)

        max_sum = float("-inf")

        for i in range(n):
            for j in range(i,n):
                sum = 0

                for k in range(i,j+1):
                    sum += arr[k]
                    max_sum = max(sum,max_sum)

        return max_sum

s1 = Solution()

arr = [2,3,5,-2,7,-4]

print(s1.kadanesBrute(arr))
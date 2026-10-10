class Solution():
    def subarrayOptimal(self,arr,k):
        n = len(arr)

        count = 0 

        prefix_sum_map = {0: 1}

        running_sum = 0 
        for i in range(n):
            running_sum += arr[i]

            rem = running_sum - k 

            if rem in prefix_sum_map:
                count += prefix_sum_map[rem]


            if running_sum in prefix_sum_map:
                prefix_sum_map[running_sum] += 1

            else:
                prefix_sum_map[running_sum] = 1

        return count
s1 = Solution()
arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k = 3

print(s1.subarrayOptimal(arr,k))
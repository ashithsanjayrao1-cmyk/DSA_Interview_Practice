import math
class Solution():
    def calculateSum(self,arr,threshold):
        n = len(arr)

        max_val = max(arr)

        for d in range(1,max_val+1):

            total_sum = 0

            for i in range(n):
                total_sum += math.ceil(arr[i]/d)

            if total_sum <= threshold:
                return d

        return -1

s1 =Solution()
arr = [1,2,5,9]
threshold = 6

print(s1.calculateSum(arr,threshold))
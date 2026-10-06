import sys

class Solution():
    def maxsubarraybruteforce(self,arr):

        max_sum = -sys.maxsize -1
        n =len(arr)

        for i in range(n):
            current_sum = 0
            for j in range(i,n):

                current_sum += arr[j]
                max_sum = max(max_sum,current_sum)

                
                # sum = 0

                # for k in range(i,j+1):

                #     sum += arr[k]

                # max_sum = max(max_sum,sum)

        return max_sum

s1 = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Brute Force:", s1.maxsubarraybruteforce(arr))
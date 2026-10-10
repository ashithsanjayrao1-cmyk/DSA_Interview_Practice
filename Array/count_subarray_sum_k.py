class Solution():
    def countsubarray(self,arr,k):

        n = len(arr)

        count = 0

        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum += arr[j]

                if current_sum == k:
                    count += 1

        return count
    
s1 = Solution()
arr = [1, 1, 1]
k = 2

print(s1.countsubarray(arr,k))


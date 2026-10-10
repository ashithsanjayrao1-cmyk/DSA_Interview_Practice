class Solution():
    def countsubarray(self,arr,k):
        n = len(arr)
        count = 0

        for i in range(n):
            for j in range(i,n):
                current_sum = 0

                for k in range(i,j+1):
                    current_sum += arr[k]


                if current_sum == k:
                    count += 1



        return count

s1 = Solution()
arr = [1, 1, 1]
k = 2

print(s1.countsubarray(arr,k))
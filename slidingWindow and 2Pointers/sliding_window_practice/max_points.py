class Solution():
    def max_points(self,arr,k):
        lsum = 0
        rsum = 0
        n = len(arr)

        max_sum = 0


        for i in range(k):
            lsum = lsum+arr[i]
            max_sum = lsum

        right_index = n-1

        for i in range(k-1,-1,-1):
            lsum = lsum - arr[i]

            rsum = rsum + arr[right_index]

            right_index -= 1


            max_sum = max(max_sum,lsum + rsum)

        return max_sum

s1 = Solution()

print(s1.max_points([1,2,3,4,5,

6],3))













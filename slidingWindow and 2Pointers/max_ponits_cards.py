class Solution():
    def maxScore(self,arr,k):
        n = len(arr)
        lsum = 0
        rsum = 0

        for i in range(k):
            lsum += arr[i]

        max_sum = lsum

        right_index = n-1

        for i in range(k - 1,-1,-1):
            lsum -= arr[i]

            rsum = rsum+arr[right_index]
            right_index -=1

            max_sum = max(max_sum,lsum+rsum)

        return max_sum

s1 = Solution()
cardPoints = [6, 2, 3, 4, 7, 2, 1, 7, 1]
k = 4

print(s1.maxScore(cardPoints,k))
    
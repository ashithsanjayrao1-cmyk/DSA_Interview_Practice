class Solution():
    def maxProduct(self,arr):
        n = len(arr)

        maxi = float('-inf')

        for i in range(n):
            product =1

            for j in range(i,n):

                product = product * arr[j]

                maxi = max(maxi,product)

        return maxi



s1 = Solution()

arr = [2,3,-2,4]

print(s1.maxProduct(arr))
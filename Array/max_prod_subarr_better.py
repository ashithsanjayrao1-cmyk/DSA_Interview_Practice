class Solution():
    def maxProductBetter(self,arr):
        n = len(arr)

        max_product = float('-inf')


        for i in range(n):

            current_prod = 1

            for j in range(i,n):

                current_prod *= arr[j]

                max_product = max(max_product,current_prod)

                #if current_prod > max_product:
                   # max_product = current_prod
                max_product = max(max_product,current_prod)

        return max_product

a1 = Solution()

arr = [2,3,-2,4]

print(a1.maxProductBetter(arr))

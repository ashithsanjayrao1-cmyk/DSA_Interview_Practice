class Solution():
    def maxProduct(self,arr):
        n = len(arr)

        max_prodcut = float('-inf')

        for i in range(n):
            for j in range(i,n):
                product = 1

                for k in range(i,j+1):
                    product = product * arr[k]

                max_prodcut = max(max_prodcut,product)


        return max_prodcut


s1 = Solution()

arr = [4,5,3,7,1,2]

print(s1.maxProduct(arr))
class Solution():
    def maxprductsubarraybruteforce(self,arr):
        n = len(arr)

        maxi = float('-inf')


        for i in range(n):
            for j in range(i,n):
                product = 1

                for k in range(i,j+1):

                    product *= arr[k]

                if product > maxi:
                    maxi = product

        return maxi
s1 = Solution()
arr = [2, 3, -2, 4]
print(s1.maxprductsubarraybruteforce(arr))





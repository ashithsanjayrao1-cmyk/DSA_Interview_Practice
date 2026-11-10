class SOlution():
    def maxProduct(self,arr):
        n = len(arr)

        prefix = 1
        suffix = 1

        maxi = float('-inf')

        for i in range(n):

            if prefix == 0:
                prefix = 1

            if suffix == 0:
                suffix = 1

            prefix = prefix * arr[i]
            suffix = suffix * arr[n-i-1]
            maxi = max(maxi,max(prefix,suffix))

        return maxi

s1 = SOlution()

arr = [2,3,-2,4]

print(s1.maxProduct(arr))
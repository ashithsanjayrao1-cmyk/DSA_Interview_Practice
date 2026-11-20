class SOlution():
    def kdanesOptimal(self,arr):
        n = len(arr)

        maxi = float("-inf")
        sum = 0

        for i in range(n):

            sum += arr[i]

            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0

        return maxi


s1 = SOlution()

arr = [2,3,5,-2,7,-4]

print(s1.kdanesOptimal(arr))
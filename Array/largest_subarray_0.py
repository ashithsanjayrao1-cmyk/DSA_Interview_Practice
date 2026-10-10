class SOlution():
    def maxBrute(slef,arr):
        n = len(arr)

        max_length = 0

        for i in range(n):
            current_sum = 0

            for j in range(i,n):
                current_sum += arr[j]

                if current_sum == 0:
                    max_length = max(max_length,j - i + 1)

        return max_length

s1 = SOlution()
arr = [15, -2, 2, -8, 1, 7, 10, 23]

print(s1.maxBrute(arr))

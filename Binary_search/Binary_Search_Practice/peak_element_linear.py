class SOlution():
    def peakELementLinear(self,arr):
        n = len(arr)
        if n == 1:
            return 0
        for i in range(n):
            if i == 0:
                if arr[i] > arr[i+1]:
                    return arr[i]

            elif i == n-1:
                if arr[i] > arr[i-1]:
                    return arr[i]
            else:

                if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                    return arr[i]
        return -1

s1 = SOlution()
print(s1.peakELementLinear([1,2,3,4,5,6,7,8,5,1]))
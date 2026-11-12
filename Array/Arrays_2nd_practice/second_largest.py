class SOlution():
    def secondLargest(self,arr):
        n = len(arr)
        largest = arr[0]
        sLargest = float('-inf')

        for i in range(n):
            if arr[i] > largest:
                sLargest = largest
                largest = arr[i]

            elif arr[i] < largest and arr[i] > sLargest:
                sLargest = arr[i]

        if sLargest == float('-inf'):
            return -1

        else:

            return sLargest

s1 = SOlution()

arr = [1,1,1,1,1]
print(s1.secondLargest(arr))

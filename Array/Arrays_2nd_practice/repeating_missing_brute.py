class SOlution():
    def repeatingMissing(self,arr):
        n = len(arr)
        repeating = -1
        missing = -1


        for i in range(1,n+1):
            count = 0

            for j in range(n):
                if arr[j] == i:
                    count+=1

            if count == 2:
                repeating = i

            elif count == 0:
                missing = i

            if repeating != -1 and missing != -1:
                break

        return repeating,missing
s1 = SOlution()
print(s1.repeatingMissing([3,1,4,5,3]))
                
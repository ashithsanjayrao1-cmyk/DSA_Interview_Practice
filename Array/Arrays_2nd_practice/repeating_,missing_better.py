class SOlution():
    def repeatingMissing(self,arr):

        n = len(arr)

        hash_map = [0] * (n+1)

        repeating = -1
        missing = -1

        for num in arr:
            hash_map[num] +=1

        for i in range(1,n+1):
            if hash_map[i] == 2:
                repeating = i
            elif hash_map[i] == 0:
                missing = i

            if repeating != -1 and missing != -1:
                break

        return[repeating,missing]
s1 = SOlution()
print(s1.repeatingMissing([1,3,4,5,1]))
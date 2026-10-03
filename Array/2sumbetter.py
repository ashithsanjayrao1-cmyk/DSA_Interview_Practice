class SOlution():
    def twosumbetter(self,arr,target):

        hash_map = {}

        for i in range(len(arr)):
            current_sum = arr[i]
            needed_sum = target - current_sum


            if needed_sum in hash_map:
                return [hash_map[needed_sum],i]


            hash_map[current_sum] = i


        return[-1,-1]

s1 = SOlution()
arr = [2, 6, 5, 8, 11]
target = 14
print(s1.twosumbetter(arr, target))


    
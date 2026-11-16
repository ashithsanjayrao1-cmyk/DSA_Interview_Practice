class SOlution():
    def majority(self,arr):

        n = len(arr)

        hash_map = {}

        for i in range(n):

            if arr[i] in hash_map:
                hash_map[arr[i]] += 1

            else:
                hash_map[arr[i]] = 1

            if hash_map[arr[i]] > n//2:
                return arr[i]

        return arr[i]
s1 = SOlution()
arr = [7,0,1,0,2,7,7,7,7,7]

print(s1.majority(arr))

class Solution():
    def fruitInaBasket(self,arr):
        n = len(arr)

        l = 0
        r = 0

        hash_map = {}

        max_len = 0


        while r < n:

            hash_map[arr[r]] = hash_map.get(arr[r],0) + 1

            while len(hash_map) > 2:
                hash_map [arr[l]] -= 1


                if hash_map[arr[l]] == 0:
                    del hash_map[arr[l]]

                l +=1

            if len(hash_map) <= 2:
                length = r-l+1
                max_len = max(max_len,length)

            r+=1
        return max_len

s1 =Solution()
print(s1.fruitInaBasket([3,3,3,1,2,1,1,2,3,3,4]))




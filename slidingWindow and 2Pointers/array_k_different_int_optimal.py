class Solution():
    def differentIntegers(self,arr:list[int],k:int) -> int:

        def atMost(k):
            if k<0:
                return 0

            n = len(arr)

            l = 0

            r = 0

            count = 0

            hash_map = {}

            while r<n:
                hash_map[arr[r]] = hash_map.get(arr[r],0)+1

                while len(hash_map) > k:

                    hash_map[arr[l]] -=1 

                    if hash_map[arr[l]] == 0:

                        del hash_map[arr [l]]
                        
                    l = l+1

                count = count + (r-l+1)
                r = r+1

            return count

        return atMost(k) - atMost(k-1)


s1 = Solution()

arr = [1,2,1,3,4]

k = 3

print(s1.differentIntegers(arr,k))








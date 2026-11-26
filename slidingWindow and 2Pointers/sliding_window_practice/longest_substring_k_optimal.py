class Solution():
    def longestSubstringK(self,arr,k):
        n = len(arr)
        max_len = 0
        hash_map = {}

        l = 0
        r = 0

        while r<n:
            hash_map[arr[r]] = hash_map.get(arr[r],0) + 1


            if len(hash_map) > k:

                hash_map[arr[l]] -= 1

                if hash_map[arr[l]] == 0:
                    del hash_map[arr[l]]

                l +=1

            if len(hash_map) <= k:  
                length = r-l+1
                max_len = max(max_len,length)
            r+=1


        return max_len
s1 = Solution()
print(s1.longestSubstringK( "aababbcaacc" , k = 2))
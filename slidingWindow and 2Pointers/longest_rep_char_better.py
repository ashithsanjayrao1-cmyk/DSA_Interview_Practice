class Solution():
    def longestRepeating(self,s:str,k:int) -> int:

        n = len(s)

        l = 0
        r = 0
        max_len = 0
        max_freq = 0
        hash_map =[0] * 26

        while r<n:

            idx = ord(s[r]) - ord('A')

            hash_map[idx] += 1

            max_freq = max(max_freq,hash_map[idx])

            while (r-l+1) - max_freq > k:

                left_idx = ord(s[l]) - ord('A')

                hash_map[left_idx] -=1


                max_freq = max(hash_map)

                l+=1

            max_len = max(max_len,r-l+1)

            r+=1
        return max_len


s1 = Solution()

print(s1.longestRepeating("AABABBA",1))


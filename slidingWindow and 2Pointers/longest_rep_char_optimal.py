class Solution():
    def CharacterReplacement(self,s:str,k:int) -> int:

        n = len(s)

        l = 0
        r = 0
        max_len = 0
        hash_arr = [0] * 26
        maxf = 0

        while r<n:
            idx = ord(s[r]) - ord('A')
            hash_arr[idx] += 1

            maxf = max(maxf,hash_arr[idx])


            if (r-l+1) - maxf > k:
                left_idx = ord(s[l]) - ord('A')

                hash_arr[left_idx]-=1

                l+=1

            if (r-l+1) - maxf <= k:
                max_len = max(max_len,r-l+1)

            r+=1

        return max_len

s1 = Solution()

print(s1.CharacterReplacement("AABABBA",1))
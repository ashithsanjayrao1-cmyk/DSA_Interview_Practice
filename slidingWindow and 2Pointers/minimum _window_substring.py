class Solution():
    def minWindow(self,s:str, t:str) -> str:

        hash_t = [0] * 256

        for char in t:
            hash_t[ord(char)] += 1

        l = 0
        r = 0
        min_len = float('inf')

        start_idx = -1

        count = 0

        m = len(t)

        n = len(s)


        while r<n:

            char_r = ord(s[r])

            if hash_t[char_r] > 0:
                count +=1

            hash_t[char_r] -= 1

            while count == m:
                if(r-l+1) < min_len:
                    min_len = r-l+1
                    start_idx = l

                char_l = ord(s[l])

                hash_t[char_l] += 1

                if hash_t[char_l] > 0:
                    count -= 1

                l += 1

            r += 1

        if start_idx == -1:
            return ""

        return s[start_idx:start_idx+min_len]


s1 = Solution()
print(s1.minWindow("ADOBECODEBANC", "ABC"))

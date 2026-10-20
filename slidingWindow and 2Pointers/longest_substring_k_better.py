class Solution():
    def longestSubstr(self,s:str,k:int) -> int:

        n = len(s)

        max_len = 0
        l = 0 
        r = 0 

        char_map = {}


        while r<n:
            char_map[s[r]] = char_map.get(s[r],0) + 1

            while len(char_map) > k:

                char_map[s[l]] -= 1

                if char_map[s[l]] == 0:
                    del char_map[s[l]]

                l+=1


            if len(char_map) <= k:
                max_len = max(max_len,r-l+1)

            r+=1

        return max_len


s1 = Solution()

print(s1.longestSubstr("eceba", 2))
                



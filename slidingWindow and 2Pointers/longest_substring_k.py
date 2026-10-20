class Solution():
    def longestSubstr(self,s: str,k:int) -> int:

        n = len(s)

        max_len = 0

        for i in range(n):
            char_map = {}

            for j in range(i,n):
                char_map[s[j]] = char_map.get(s[j],0) +1

                if len(char_map) >k:
                    break

                if len(char_map) <= k:
                    max_len = max(max_len,j-i+1)

        return max_len


s1 = Solution()
print(s1.longestSubstr("eceba", 2))


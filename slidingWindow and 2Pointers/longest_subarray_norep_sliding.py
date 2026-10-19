class Solution():

    def lengthOfLongestSubstring(self,s:str) -> int:

        n = len(s)

        hash_arr = [-1] * 256

        l = 0
        r = 0

        max_len = 0

        while r<n:

            char_ascii = ord(s[r])

            if hash_arr[char_ascii] != -1:
                if hash_arr[char_ascii] >= l:
                    l = hash_arr[char_ascii] +1


            length = r-l+1
            max_len = max(length,max_len)

            hash_arr[char_ascii] = r

            r+=1

        return max_len

s1 = Solution()
print(s1.lengthOfLongestSubstring("cadbzabcd"))


class Solution():
    def longestSubstring(self,string):
        n = len(string)
        l = 0
        r = 0
        max_sum = 0
        hash_array = [0] * 256

        while r < n:
            char_ascii = ord(string[r])

            if hash_array[char_ascii] != -1:
                if hash_array[char_ascii] >= l:
                    l = hash_array[char_ascii] + 1

            length = r-l+1
            max_sum = max(max_sum,length)
            hash_array[char_ascii] = r
            r += 1

        return max_sum

s1 = Solution()
print(s1.longestSubstring('cadbzabcd'))
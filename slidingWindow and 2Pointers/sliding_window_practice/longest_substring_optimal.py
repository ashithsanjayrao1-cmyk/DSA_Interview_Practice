class Solution():
    def longestSubstring(self,string):
        n = len(string)
        hash_arr = [0] * 256

        l = 0
        r = 0

        max_len = 0

        while r < n:

            char_asci = ord(string[r])

            if hash_arr[char_asci] != -1:
                if hash_arr[char_asci] > l:
                    l = hash_arr[char_asci] + 1

            length = r-l+1
            max_len = max(max_len,length)

            hash_arr[char_asci] = r


            r+=1
        return max_len

s1 = Solution()
print(s1.longestSubstring('cadbzabcd'))



        
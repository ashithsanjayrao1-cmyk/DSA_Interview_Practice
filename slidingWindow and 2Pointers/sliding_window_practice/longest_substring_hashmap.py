class Solution():
    def longestSubstring(self,string):
        n = len(string)
        max_len = 0

        for i in range(n):

            hash_map = [0] * 256

            for j in range(i,n):

                if hash_map[ord(string[j])] == 1:
                    break
                length = j-i+1
                max_len = max(max_len,length)
                hash_map[ord(string[j])] = 1

        return max_len

s1 = Solution()

s = "cadbzabcd"

print(s1.longestSubstring(s))
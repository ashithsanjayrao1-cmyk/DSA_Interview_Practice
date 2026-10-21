class Solution():
    def minWindow(self,s:str,t:str)-> str:

        n = len(s)
        m = len(t)

        if m>n or m == 0:
            return ""

        min_len = float('inf')

        start_idx = -1


        for i in range(n):

            hash_t = [0]*256

            for char in t:

                hash_t[ord(char)] += 1

            count = 0

            for j in range(i,n):
                char_idx = ord(s[j])

                if hash_t[char_idx] > 0:
                    count+=1

                hash_t[char_idx] -= 1

                if count == m:

                    if (j-i+1) < min_len:
                        min_len = j-i+1
                        start_idx = i

                    break


        if start_idx == -1:
            return ""

        return s[start_idx : start_idx + min_len]


s1 = Solution()
print(s1.minWindow("ADOBECODEBANC", "ABC"))
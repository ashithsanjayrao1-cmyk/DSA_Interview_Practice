class Solution():
    def characterReplacement(self,s:str,k:int) -> int:
        n = len(s)

        max_len = 0

        for i in range(n):
            hash_map = [0] * 26
            max_freq = 0

            for j in range(i,n):

                idx = ord(s[j]) - ord('A')

                hash_map[idx] +=1

                max_freq = max(max_freq,hash_map[idx])

                changes = (j-i+1) - max_freq

                if changes <=k:
                    max_len = max(max_len,j-i+1)

                else:

                    break

        return max_len
                
s1 = Solution()
print(s1.characterReplacement("AABABBA", 1))
class Solution():
    def CharString(self,s:str) -> int:

        n = len(s)



        last_seen = [-1,-1,-1]
        count = 0

        for i in range(n):

            char_idx = ord(s[i]) - ord ('a')

            last_seen[char_idx] = i

            if last_seen[0] != -1 and last_seen[1] !=-1 and last_seen[2] !=-1:

                minimum_index = min(last_seen)

                count += (minimum_index + 1)


        return count


s1 = Solution()

print(s1.CharString(s= "bbacba"))
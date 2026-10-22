class Solution():
    def AllCharacters(self,s:str) ->int:

        n = len(s)

        count = 0

        for i in range(n):
            hash_map = [0] * 3

            for j in range(i,n):
                hash_map[ord(s[j]) - ord('a')] = 1

                if hash_map[0] + hash_map[1] + hash_map[2] == 3:
                    count += (n-j)
                    break



        return count


s1 = Solution()

print(s1.AllCharacters(s="bbacba"))
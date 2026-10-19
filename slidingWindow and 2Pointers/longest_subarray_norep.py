class Solution():
    def longestSub(self,s:str) ->int:
        n=len(s)
        max_len = 0

        for i in range(n):

            hash_array = [0] * 256

            for j in range(i,n):

                if hash_array[ord(s[j])] == 1:
                    break

                length = j-i+1

                max_len = max(max_len,length)

                hash_array[ord(s[j])] = 1
                

        return max_len

s1 = Solution()

print(s1.longestSub('cadbzabcd'))


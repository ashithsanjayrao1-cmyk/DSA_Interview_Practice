class Solution():
    def minimumWindow(self,arr,t):

        n = len(arr)
        m = len(t)
        min_len = float('inf')


        start = -1

        for i in range(n):
            hash_t = [0] * 256

            for char in t:
                hash_t[ord(char)] +=1 

            count = 0


            for j in range(i,n):
                char_idx = ord(arr[j])

                if hash_t[char_idx] > 0:
                    count += 1

                hash_t [char_idx] -=1

                if count == m:
                    if (j-i+1) < min_len:
                        min_len = (j-i+1)
                        start = i

                    break

            if start == -1:
                return ""

            return arr[start : start+min_len]
s1 = Solution()
print(s1.minimumWindow("ADOBECODEBANC", "ABC"))
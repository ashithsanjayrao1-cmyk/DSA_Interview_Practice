class Solution():
    def minimum_window(self,s,t):
        min_len = float('inf')
        count = 0

        l = 0
        r = 0

        m = len(t)

        n = len(s)

        start_index = -1

        hash_arr = [0] * 256

        for char in t:
            hash_arr[ord(char)] += 1

        count = 0

        while r < n:

            if hash_arr[ord(s[r])] > 0:
                count += 1

            hash_arr[ord(s[r])] -= 1

            while count == m:
                length = r-l+1

                if length < min_len:
                    min_len = length
                    start_index = l

                hash_arr[ord(s[l])] +=1
                if hash_arr[ord(s[l])] > 0:
                    count -=1

                l +=1


            r = r+1

        if start_index == -1:
            return ""

        return s[start_index : start_index + min_len]

s1 = Solution()
print(s1.minimum_window("ADOBECODEBANC", "ABC"))


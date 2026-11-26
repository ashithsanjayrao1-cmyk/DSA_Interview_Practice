class Solution():
    def longestRepeating(self,arr,k):
        n = len(arr)
        hash_map = [0] * 26
        l = 0
        r = 0
        max_len = 0
        max_freq = 0

        while r < n:

            idx = ord(arr[r]) - ord('A')

            hash_map[idx] +=1 

            max_freq = max(max_freq,hash_map[idx])

            if (r-l+1) - max_freq > k:
                left_idex = ord(arr[l]) - ord('A')
                hash_map[left_idex] -= 1

                max_freq = max(hash_map)
                l +=1
            max_len = max(max_len,r-l+1)
            r+=1
        return max_len

s1 = Solution()
print(s1.longestRepeating('AABABBA',1))
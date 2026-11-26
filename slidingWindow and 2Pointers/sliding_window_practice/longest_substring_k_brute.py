class Soution():
    def longestSubstrignK(self,arr,k):
        n = len(arr)
        max_len = 0

        for i in range(n):
            bucket = set()

            for j in range(i,n):
                bucket.add(arr[j])

                if len(bucket) <= k:
                    length = j-i+1
                    max_len = max(max_len,length)

            else:
                break

        return max_len

s1 = Soution()
print(s1.longestSubstrignK("abcddefg" , k = 3))
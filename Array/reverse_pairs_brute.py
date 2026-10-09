class Solution():
    def reversepairs(self,arr):
        n = len(arr)

        count = 0

        for i in range(n):
            for j in range(i+1,n):
                if arr[i] > 2*arr[j]:
                    count += 1

        return count


s1 = Solution()

arr = [40,25,19,12,9,6,2]

print(s1.reversepairs(arr))
class Solution():
    def count_inversions(self,arr):
        n = len(arr)
        count = 0

        for i in range(n):
            for j in range(i+1,n):
                if arr[i] > arr[j] and i < j:
                    count += 1
        return count
s1 = Solution()
print(s1.count_inversions([2,3,7,1,3,5]))

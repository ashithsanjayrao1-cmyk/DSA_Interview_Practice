class Solution():
    def countInversion(self,arr):
        n = len(arr)

        count = 0

        for i in range(n):
            for j in range(i+1,n):
                if arr[i] > arr[j]:
                    count+=1

        return count


s1 = Solution()

arr = [2,3,7,1,3,5]

print(s1.countInversion(arr))


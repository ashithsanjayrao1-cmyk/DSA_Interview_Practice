class Solution():
    def countInversions(self,arr):
        n = len(arr)

        count = 0

        for i in range(n):
            for j in range(i+1,n):
                if arr[i] > arr[j]:
                    count +=1

        return count


s1 = Solution()

arr = [5,3,2,4,1]

print(s1.countInversions(arr))
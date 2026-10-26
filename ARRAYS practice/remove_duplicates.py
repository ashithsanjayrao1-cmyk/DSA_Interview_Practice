class Solution():
    def removeDuplicates(self,arr):
        n = len(arr)
        if n == 0:
            return 0

        i = 0

        for j in range(1,n):
                if arr[j] != arr[i]:
                     arr[i+1] = arr[j]
                     i += 1


        return i + 1
                                     

s1 = Solution()
print(s1.removeDuplicates(arr=[1,1,2,2,2,3,3,3]))                       
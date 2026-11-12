class Solution():
    def linearSearch(self,arr,target):

        n = len(arr)

        for i in range(n):
            if arr[i] == target:
                return i

        return -1

s1 = Solution()

arr = [3,4,5,7,9,10]
print(s1.linearSearch(arr,30))
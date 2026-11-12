class Solution():
    def largestElement(self,arr):
        n = len(arr)

        largest = float('-inf')

        for i in range(n):

            if arr[i] > largest:
                largest = arr[i]

        return largest

s1 = Solution()

arr = [2,3,4,5,6,999999]

print(s1.largestElement(arr))
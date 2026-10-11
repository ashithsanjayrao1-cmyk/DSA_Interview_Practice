class Solution():
    def singleelementbrute(self,arr):

        n = len(arr)

        for i in range(n):
            if i == 0:
                if arr[i] != arr[i+1]:
                    return arr[i]

            elif i == n-1:
                if arr[i] != arr[i-1]:
                    return arr[i]

            else:
                if arr[i]!=arr[i+1] and arr[i]!=arr[i-1]:
                    return arr[i]

s1 = Solution()
nums = [1, 1, 2, 2, 3, 4, 4, 5, 5]

print(s1.singleelementbrute(nums))
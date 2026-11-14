class Solution():
    def twoSum(self,arr,target):

        n = len(arr)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if arr[i] + arr[j] == target:
                    return (i,j)

        return (i,j)


s1 = Solution()
target = 7
arr = [1,6,2,10,3]

print(s1.twoSum(arr,target))
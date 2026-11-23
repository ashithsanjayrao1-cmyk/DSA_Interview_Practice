class Solution():
    def twoSum(self,arr,target):
        n = len(arr)

        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j] == target:
                    return i,j

        return -1

s1 = Solution()
print(s1.twoSum([3,7,3,8,11],6))                
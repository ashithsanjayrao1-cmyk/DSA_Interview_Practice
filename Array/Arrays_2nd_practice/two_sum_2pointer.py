class Solution():
    def twoSum(self,arr,target):
        n = len(arr)
        left = 0
        right = n-1
        arr.sort()

        while left < right:
            sum = arr[left] + arr[right]

            if sum == target:
                return left,right
            elif sum < target:
                left+=1
            else:
                right-=1

        return -1

s1 = Solution()
print(s1.twoSum([2,5,6,8,11],14))

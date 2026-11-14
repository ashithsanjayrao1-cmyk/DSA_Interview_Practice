class Solution():
    def twoSum(self,arr,target):

        arr.sort()

        n = len(arr)

        left = 0
        right = n-1

        while left<right:
            sum = arr[left]+arr[right]

            if sum == target:
                return "YES"

            elif sum < target:
                left += 1

            else:
                right -= 1

        return "NO"

s1 = Solution()
target = 7
arr = [1,6,2,10,3]

print(s1.twoSum(arr,target))
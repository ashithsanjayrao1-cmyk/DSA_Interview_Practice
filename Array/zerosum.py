class Solution():
    def twoSumOptimal(self,arr,target):
        n = len(arr)

        arr.sort()

        left = 0
        right = n-1

        while left < right:
            current_sum = arr[left] + arr[right]


            if current_sum == target:
                return "YES"

            elif current_sum < target:
                left +=1

            else:
                right -= 1

        return "NO"

s1 = Solution()
arr = [2, 6, 5, 8, 11]
target = 14

print(s1.twoSumOptimal(arr, target))
class Solution():

    def consecutiveones(self,nums):
        n = len(nums)

        maxi = 0 
        count = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1

                maxi = max(count,maxi)

            else:
                count = 0

        return maxi


s1 = Solution()

nums = [1,1,2,3,1,1,1,2,3,1,1,1,1,1]

print(s1.consecutiveones(nums))


class Solution():

    def countSubarrays(self,nums,mimit):
        subarray = 1
        current_sum = 0
        for num in nums:
            if current_sum + num > mimit:
                subarray += 1
                current_sum = num
            else:
                current_sum += num

        return subarray

    def splitArray(self,nums,k):

        if k>len(nums):
            return -1

        low = max(nums)

        high = sum(nums)
        ans = -1

        while low <= high:

            mid = (low+high)//2

            if self.countSubarrays(nums,mid) <= k:
                ans = mid 
                high = mid-1

            else:
                low = mid+1

        return ans
s1 = Solution()
nums = [7, 2, 5, 10, 8]
k = 2

print(s1.splitArray(nums,k))



    
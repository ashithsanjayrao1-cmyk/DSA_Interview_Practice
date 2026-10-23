class Solution():
    def numSubarrayWithSum(self,nums: list[int],goal: int) -> int:
 

        def atMost(k):
            if k < 0:

                return 0

            n = len(nums)
            l = 0 
            r = 0

            current_sum = 0
            count = 0

            while r < n:
                current_sum += nums[r]

                while current_sum > k:
                    current_sum -= nums[l]

                    l+=1

                count += (r-l+1)
                r += 1

            return count

        return atMost(goal) - atMost(goal-1)


s1 = Solution()
print(s1.numSubarrayWithSum([1,0,1,0,1], 2))
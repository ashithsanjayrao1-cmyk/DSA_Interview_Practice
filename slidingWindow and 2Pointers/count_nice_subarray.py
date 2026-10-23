class Solution():
    def countSubarray(self,nums: list[int],goal:int) -> int:

        def atMost(k):
            if k<0:
                return 0 
        
            n = len(nums)

            l = 0
            r = 0
            count = 0

            current_sum = 0

            while r<n:

                current_sum += nums[r] % 2

                while current_sum > k:
                    current_sum -= nums[l] % 2
                    l+=1

                count += (r-l+1)
                r += 1

            return count


        return atMost(goal) - atMost(goal-1)


s1 = Solution()

arr = [1,1,2,1,1]

print(s1.countSubarray(arr,goal=3))


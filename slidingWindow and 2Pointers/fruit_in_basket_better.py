class Solution():

    def totalFruits(self,fruits: list[int]) -> int:
        n = len(fruits)

        l = 0
        r = 0

        max_len = 0

        fruits_count = {}

        while r<n:

            fruits_count[fruits[r]] = fruits_count.get(fruits[r],0) + 1

            if len(fruits_count) > 2:

                fruits_count[fruits[l]] -= 1

                if fruits_count[fruits[l]] == 0:
                    del fruits_count[fruits[l]]

                l+=1

            if len(fruits_count) <= 2:
                max_len = max(max_len,r-l+1)

            r+=1

        return max_len





s1 = Solution()
fruits = [1, 2, 1, 2, 3]
print(s1.totalFruits(fruits))   
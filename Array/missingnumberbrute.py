class Solution():
    def findMissingRepeatingBruteForce(self,arr):
        n = len(arr)

        missing = -1
        repeating = -1

        for i in range(1,n+1):
            count = 0

            for j in range(n):
                if arr[j] == i:
                    count += 1


            if count == 2:
                repeating = i

            elif count == 0:
                missing = i

            if repeating != -1 and missing != -1:
                break


        return [repeating,missing]

s1 = Solution()
arr = [3, 1, 2, 5, 3]
print(s1.findMissingRepeatingBruteForce(arr))
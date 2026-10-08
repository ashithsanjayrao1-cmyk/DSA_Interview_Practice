class Solution():
    def missingRepeatingBetter(self,arr):
        n = len(arr)

        hash_arr = [0] * (n+1)

        missing =-1
        repeating = -1

        for num in  arr:
            hash_arr[num] += 1

        for i in range(1,n+1):
            if hash_arr[i] == 2:
                repeating = i
            elif hash_arr[i] == 0:
                missing = i

            if repeating != -1 and missing != -1:
                break

        return [repeating,missing]
s1 = Solution()
arr = [3, 1, 2, 5, 3]
print(s1.missingRepeatingBetter(arr))
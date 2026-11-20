class Solution():
    def maxOnes(self,arr):
        n = len(arr)
        count = 0
        max_ones = 0

        for i in range(n):
            if arr[i] == 1:
                count += 1

                if max_ones < count:
                    max_ones = count

            else:
                count = 0


        return max_ones


s1 = Solution()


arr = [ 1,1,0,0,1,1,1,0]
print(s1.maxOnes(arr))
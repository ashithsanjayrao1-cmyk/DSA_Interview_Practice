class Solution():
    def jumpGame(self,arr):
        n = len(arr)

        max_index = 0

        for i in range(n):
            if i > max_index:
                return False

            max_index = max(max_index,i+arr[i])

        return True

s1 = Solution()
print(s1.jumpGame([1,2,3,1,1,0,2,5]))
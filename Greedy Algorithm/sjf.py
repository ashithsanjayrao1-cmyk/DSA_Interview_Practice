class Solution():
    def SJF(self,arr):
        n = len(arr)
        arr.sort()
        time = 0
        waiting_time = 0

        for i in range(n):
            waiting_time += time

            time += arr[i]

        return waiting_time//n

s1 = Solution()
print(s1.SJF([4,3,7,1,2]))
class Solution():
    def Majority(self,arr):
        n = len(arr)

        for i in range(n):
            count = 0
            for j in range(n):
                if arr[i] == arr[j]:
                    count += 1

            if count > n//2:
                return arr[i]



s1 = Solution()

arr = [7,0,0,1,7,7,2,7,7]

print(s1.Majority(arr))
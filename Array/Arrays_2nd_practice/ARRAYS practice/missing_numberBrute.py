class Solution():
    def missingNumber(self,arr):
        n = len(arr)
        ans = 0

        for i in range(n):
            flag = 0
            for j in range(n):
                if arr[j] == i:
                    flag = 1
                    break
            if flag == 0:

                return i 

s1 = Solution()
arr = [0,1,2,4,5]

print(s1.missingNumber(arr))

            


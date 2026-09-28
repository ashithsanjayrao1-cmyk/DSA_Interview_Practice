class Solution():
    def missingnumber(self,arr):
        n = len(arr)


        sum = n * (n+1) // 2

        s2 = 0

        for i in range(n):
            s2 += arr[i]

        return sum - s2


        # for i in range(n):
        #     flag = 0
            
        #     for j in range(n-1):
                
        #         if arr[j] == i:

        #             flag = 1
        #             break

        #     if flag == 0:
        #         return i


s1 = Solution()

arr = [0,1,3,4,5]

print(s1.missingnumber(arr))


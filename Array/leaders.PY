class Solution():
    def leaders(self,arr):
        n = len(arr)

        ans = []

        maxi = float('-inf')

        for i in range(n-1,-1,-1):

            if arr[i] >= maxi:
                ans.append(arr[i])

                maxi = arr[i]


        #ans.reverse()
        return ans
    


        # for i in range(n):
        #     leader = True

        #     for j in range(i+1,n):
        #         if arr[j] >= arr[i]:
        #             leader = False
        #             break


        #     if leader == True:
        #         ans.append(arr[i])

        # return ans
    

s1 = Solution()

arr = [10,22,12,3,0,6]

print(s1.leaders(arr))


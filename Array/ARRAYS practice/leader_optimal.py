class Solution():
    def leader(self,arr):
        n = len(arr)

        ans =[]
        maxi = float('-inf')


        for i in range(n-1,-1,-1):

            if arr[i] > maxi:
                maxi = arr[i]

                ans.append(arr[i])
                ans.sort(reverse=True)

        return ans
    



s1 = Solution()

arr = [1,2,5,3,1,2]


print(s1.leader(arr))

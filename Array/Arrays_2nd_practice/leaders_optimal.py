class Solution():
    def leadears(self,arr):
        n = len(arr)

        maxi = float('-inf')
        ans = []

        for i in range(n-1,-1,-1):
            if arr[i] > maxi:
                maxi = arr[i]

                ans.append(arr[i])

        ans.reverse()
        return ans
    
            

                
s1 = Solution()
print(s1.leadears([1,2,5,3,1,2]))
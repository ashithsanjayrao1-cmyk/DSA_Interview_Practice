class Solution():
    def leadrers(self,arr):
        n = len(arr)
        ans = []


        for i in range(n):
            leaders = True

            for j in range(i+1,n):
                if arr[j] > arr[i]:
                    leaders = False


                    break

            if leaders == True:
                ans.append(arr[i])

        return ans
    


s1 = Solution()

arr = [1,2,5,3,1,2]

print(s1.leadrers(arr))


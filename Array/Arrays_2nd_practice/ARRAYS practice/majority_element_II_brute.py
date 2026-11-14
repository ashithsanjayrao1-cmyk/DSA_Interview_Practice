class Solution():

    def majorityElement(self,arr):

        n = len(arr)
        ans = []

        threeshold = n//3

        for i in range(n):

            if arr[i] not in ans:
                count = 0

                for j in range(n):
                    if arr[j] == arr[i]:
                        count += 1

                if count > threeshold:
                    ans.append(arr[i])

                
                if len(ans) == 2:
                    break



                

        return ans


s1 = Solution()
arr = [1,1,1,3,3,2,2,2]

print(s1.majorityElement(arr))

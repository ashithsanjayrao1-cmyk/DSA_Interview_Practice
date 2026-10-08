class Solution():
    def majorityElementII(self,arr):
        n = len(arr)
        ans = []

        treshold = n //3

        for i in range(n):
            if arr[i] not in ans:
                count = 0

                for j in range(n):
                    if arr[i] == arr[j]:
                        count +=1


                if count > treshold:
                    ans.append(arr[i])


                if len(ans) == 2:
                    break


        return ans

s1 = Solution()
arr = [11, 33, 33, 11, 33, 11, 2, 2, 3, 3, 2, 11, 33,2,11,11]
print(s1.majorityElementII(arr))       
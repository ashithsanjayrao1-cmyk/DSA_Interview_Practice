class Solution():
    def majorituElement(self,arr):
        n = len(arr)

        ans = []

        threshold = n//3

        for i in range(n):
            if arr[i] not in ans:
                count = 0

                for j in range(n):
                    if arr[j] == arr[i]:
                        count+=1

                if count > threshold:
                    ans.append(arr[i])

                if len(arr) == 2:
                    break
        return ans
    
s1 = Solution()
print(s1.majorituElement([1,2,3,1,1,2]))
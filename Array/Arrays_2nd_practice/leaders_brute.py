class Solution():

    def leaders(self,arr):
        n = len(arr)
        ls = []

        for i in range(n):
            for j in range(i+1,n):
                if arr[i] < arr[j]:

                    break
            else:
                ls.append(arr[i])

        return ls
s1 = Solution()

print(s1.leaders([1,2,5,3,1,2]))
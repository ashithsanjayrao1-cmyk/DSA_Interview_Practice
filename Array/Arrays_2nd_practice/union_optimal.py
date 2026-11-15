class Solution():
    def union(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        ans = []
        i = 0
        j = 0

        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                if len(ans) == 0 or ans[-1] != arr1[i]:

                    ans.append(arr1[i])
                i += 1
            else:
                if len(ans) == 0 or ans[-1] != arr2[j]:
                    ans.append(arr2[j])
                j += 1

        while i < n1:
            if len(ans) == 0 or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i+=1
        while j <n2:
            if len(ans) == 0 or ans[-1] != arr2[j]:
                ans.append(arr2[j])

            j += 1
        return ans

s1 = Solution()
print(s1.union(arr1=[1,2,3,4,5,6],arr2=[2,3,4,5,6,6,7]))
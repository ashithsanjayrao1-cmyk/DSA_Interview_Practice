class Solution():
    def intersection(self,arr1,arr2):

        n1 = len(arr1)
        n2 = len(arr2)



        i = 0
        j = 0
        ans = []

        while i<n1 and j <n2:
            if arr1[i] < arr2[j]:
                i+= 1

            elif arr2[j] < arr1[j]:
                j += 1

            else:
                ans.append(arr2[j])

                i += 1
                j += 1

        return ans


s1 = Solution()

arr1 = [1,2,2,3,3,4,5,6]
arr2 = [2,3,3,5,6,6,7]

print(s1.intersection(arr1,arr2))
class Solution():
    def unionsorted(self,arr1,arr2):

        n1 = len(arr1)
        n2 = len(arr2)

        i = 0
        j = 0

        union_arr = []

        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
                    union_arr.append(arr1[i])

                i += 1

            else:
                if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
                    union_arr.append(arr2[j])

                j += 1

        while i < n1:
            if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])

            i += 1

        while j < n2:
            if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])

            j += 1

        return union_arr
       



s1 = Solution()
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]

print(s1.unionsorted(arr1, arr2))
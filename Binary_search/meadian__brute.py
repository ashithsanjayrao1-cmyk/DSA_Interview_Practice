class Solution():
    def median(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        ans = []
        i = 0
        j = 0

        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1

        while i < n1:
            ans.append(arr1[i])
            i += 1
        while j < n2:
            ans.append(arr2[j])
            j += 1


        n = n1 + n2
        if n % 2 == 1:
            return float(ans[n//2])

        else:
            return (ans[n//2] + ans[(n//2)-1])/2
s1 = Solution()

print(s1.median([1,3,5,7,9,11],[2,4,6,8]))

        
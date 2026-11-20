class Solution():

    def merege2(self,arr1,arr2):
        n = len(arr1)
        m = len(arr2)

        left = n-1
        right = 0

        while left >= 0 and right <= m:
            if arr1[left] > arr2[right]:
                arr1[left],arr2[right] = arr2[right],arr1[left]
                left-=1
                right += 1
            else:
                break

        arr1.sort()
        arr2.sort()

        return arr1,arr2


s1 = Solution()

arr1 =  [-5, -2, 4, 5, 0, 0, 0]
arr2 = [-3, 1, 8]

print(s1.merege2(arr1,arr2))
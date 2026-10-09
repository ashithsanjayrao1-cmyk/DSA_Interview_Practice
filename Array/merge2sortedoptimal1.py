class Solution():
    def merge2sortedoptimal(self,arr1,arr2,n,m):
        n = len(arr1)
        m = len(arr2)

        left = n-1
        right = 0

        while left >= 0 and right < m:
            if arr1[left] > arr2[right]:
                arr1[left],arr2[right] = arr2[right],arr1[left]

                left -= 1
                right += 1
            else:
                break



        arr1.sort()
        arr2.sort()

        return arr1,arr2


s1 = Solution()

arr1 = [1,4,7,8,10]

arr2 = [2,3,9]

print(s1.merge2sortedoptimal(arr1,arr2,len(arr1),len(arr2)))
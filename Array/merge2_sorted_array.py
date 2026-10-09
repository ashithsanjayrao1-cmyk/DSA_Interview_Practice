class Solution():
    def merge(self,arr1,arr2,n,m):

        n = len(arr1)
        m = len(arr2)


        arr3 = [0] * (n+m)

        left = 0
        right = 0
        index = 0

        while left < n and right < m:
            if arr1[left] <= arr2[right]:
                arr3[index] = arr1[left]

                left += 1
                index += 1

            else:
                arr3[index] = arr2[right]
                right += 1
                index += 1

        while left < n:
            arr3[index] = arr1[left]
            left += 1
            index += 1

        while right < m:
            arr3[index] = arr2[right]
            right += 1
            index += 1


        for i in range(n + m):
            if i < n:
                arr1[i] = arr3[i]

            else:
                arr2[i-n] = arr3[i]

        return arr3

s1 = Solution()

arr1 = [1,4,7,8,10]

arr2 = [2,3,9]


print(s1.merge(arr1,arr2,len(arr1),len(arr2)))
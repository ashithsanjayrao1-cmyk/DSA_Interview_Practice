class Solution():
    def secondLar(self,arr):
        n = len(arr)

        if n < 2:
            return -1

        arr.sort()


        largest = arr[-1]

        for i in range(n-2,-1,-1):

            if arr[i] != largest:
                return arr[i]


        return -1


s1 = Solution()

arr = [1,4,4,6,2,7,9,11,0,27]

print(s1.secondLar(arr))

    
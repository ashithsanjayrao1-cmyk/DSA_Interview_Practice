class Solution():
    def largestEle(self,arr):
        n = len(arr)

        largest = arr[0]

        for i in range(n):

            if arr[i] > largest:
                largest = arr[i]


        print(largest)


s1 = Solution()

arr = [3,3,0,99,99,-40]

s1.largestEle(arr)
            
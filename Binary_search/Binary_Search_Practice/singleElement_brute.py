class Solution():
    def singleElement(self,arr):

        n = len(arr)
        if n==1:
            return  arr

        for i in range(n):
            if i == 0:

                if arr[i] != arr[i+1]:
                    return arr[i]


            elif i == n-1:
                if arr[i] != arr[i-1]:

                    return arr[i]

            else:

                if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
                    return arr[i]




s1 = Solution()

arr = [1]                     

print(s1.singleElement(arr))


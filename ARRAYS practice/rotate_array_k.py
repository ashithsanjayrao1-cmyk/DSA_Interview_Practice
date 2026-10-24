class Solution():
    def kLeftShift(self,arr,k):

        n = len(arr)

        if n==0:
            return arr

        k = k %n

        def reverse(start,end):
            while start<end:
                arr[start],arr[end] = arr[end],arr[start]

                start += 1
                end -= 1

        reverse(0,k-1)
        reverse(k,n-1)

        reverse(0,n-1)

        return arr


s1 = Solution()

arr = [1,2,3,4,5,6,7]
d = 3

print(s1.kLeftShift(arr,d))
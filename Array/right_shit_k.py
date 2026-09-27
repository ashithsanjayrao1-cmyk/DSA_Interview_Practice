class Solution():
    def reverse(self,arr,start,end):
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]

            start += 1
            end -= 1

    def rightshift(self,arr,k):

        n = len(arr)

        k = k % n
        if k == 0:
            return 

        self.reverse(arr,0,n-1)

        self.reverse(arr,0,k-1)

        self.reverse(arr,k,n-1)

        return arr

s1= Solution()

arr = [1,2,3,4,5]

k = 2
print(s1.rightshift(arr,k))

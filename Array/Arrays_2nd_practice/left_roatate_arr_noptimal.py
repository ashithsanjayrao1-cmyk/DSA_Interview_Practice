class Solution():

    def reverse(self,arr,start,end):
        while start < end:

            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -=1

    def leftrotate(self,arr,d):
        n = len(arr)
        d = d%n
        if d == 0:
            return 

        self.reverse(arr,0,d-1)
        
        self.reverse(arr,d,n-1)

        self.reverse(arr,0,n-1)

        return arr

s1 = Solution()
arr = [1,2,3,4,5,6,7]
print(s1.leftrotate(arr,3))
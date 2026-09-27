class Solution():
    # def leftshiftk(self,arr,d):
        # n = len(arr)
        # d = d % n

        # if d == 0:
        #     return arr

        # temp = []

        # for i in range(d):
        #     temp.append(arr[i])

        # for i in range(d,n):
        #     arr[i-d] = arr[i]

        # for i in range(d):
        #     arr[n-d+i] = temp[i]

        # return arr

    def reverse(self,arr,start,end):
        while start < end:
            arr[start], arr[end] = arr[end],arr[start]
            start += 1
            end -= 1

    def leftshift(self,arr,d):
        n=len(arr)

        d = d % n

        if d == 0:
            return arr


        self.reverse(arr,0,d-1)

        self.reverse(arr,d,n-1)

        self.reverse(arr,0,n-1)

        return arr
    
        

s1 = Solution()

arr = [1,2,3,4,5]

d = 2

print(s1.leftshift(arr,d))
            
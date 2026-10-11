class Solution():
    def firstLastOccurance(self,arr,x):
        n = len(arr)

        first = -1
        last = -1

        for i in range(n):
            if arr[i] == x:
                if first == -1:
                    first = i
                    

                else:
                    last = i
                    


        return first,last

s1 = Solution()

arr = [1,2,3,4,5,5,6,5]

x=5

print(s1.firstLastOccurance(arr,x))
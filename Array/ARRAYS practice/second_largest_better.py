class Solution():
    def secondLargest(self,arr):
        n = len(arr)

        if n<2:
            return -1

        largest = arr[0]

        for i in range(1,n):
            if arr[i] > largest:
                largest = arr[i]



        slargest = float('-inf')

        for i in range(n):
            if arr[i] != largest and arr[i] > slargest:

                slargest = arr[i]
                return slargest
        return -1
    
        

    
            

       

s1 = Solution()

arr = [3,3,3,3,1]

print(s1.secondLargest(arr))

            

        

    
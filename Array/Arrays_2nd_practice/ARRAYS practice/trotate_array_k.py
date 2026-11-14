class Solution():
    def kLeftShift(self,nums,k):
        n = len(nums)
        temp = []

        k = k%n

        for i in range(k):
            temp.append(arr[i])

        for i in range(k,n):

            nums[i-k] = arr[i]

        for i in range(k):                                        
            nums[n-k + i] = temp[i]

        return nums



 
 


s1 = Solution()

arr = [1,2,3,4,5,6]
k = 2

print(s1.kLeftShift(arr,k))
    
class Solution():
    def nextPermutation(self,arr):
        n = len(arr)

        dip_index = -1


        for i in range(n-2,-1,-1):
            if arr[i] < arr[i+1]:
                dip_index = i
                break
        if dip_index == -1:
            arr.reverse()
            return arr

        for i in range(n-1,dip_index,-1):
            if arr[i] > arr[dip_index]:
                arr[i],arr[dip_index] = arr[dip_index],arr[i]
                break
        arr[dip_index+1:] = reversed(arr[dip_index+1:])
        return arr

s1 = Solution()
print(s1.nextPermutation([2,1,5,4,3,0,0]))
            

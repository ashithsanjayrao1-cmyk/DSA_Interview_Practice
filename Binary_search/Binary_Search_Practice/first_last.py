class Solution():
    def firstLast(self,arr,target):

        n = len(arr)
        first = -1
        last = -1

        for i in range(n):
            if arr[i] == target:

                if first == -1:
                    first = i

                else:
                    last = i
            

        return[first,last]
    
            

        


s1 = Solution()

arr = [2,4,6,8,8,8,11,13]

print(s1.firstLast(arr,8))
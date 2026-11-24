class Solution():
    def dutchNationalAlgorith(self,arr):
        n = len(arr)
        mid = 0
        low = 0
        high = n-1


        while mid <= high:

            if arr[mid] == 0:

                arr[low],arr[mid] = arr[mid],arr[low]
                low+=1
                mid+=1

            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid],arr[high] = arr[high],arr[mid]

                high -=1
        return arr
s1 = Solution()
print(s1.dutchNationalAlgorith([2,1,0,1,0,1,2,1,0,0,2,1,0,2,1,1,0,0,1]))
    


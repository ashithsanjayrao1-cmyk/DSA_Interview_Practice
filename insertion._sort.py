class Solution():

    
    def insertion_sort(self,arr):
        n = len(arr)

        for i in range(n):
            j = i 

            while j > 0 and arr[j-1] > arr[j]:

                #arr[j-1],arr[j] = arr[j],arr[j-1]
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp


                j -= 1

        return arr

s1 = Solution()

n_1 = [10,4,5,7,8,2,1]

print(s1.insertion_sort(n_1))
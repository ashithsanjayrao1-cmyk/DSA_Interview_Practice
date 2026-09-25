class Solution():
    def selection_sort(self,arr):

        n = len(arr)

        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                

                if arr[j] < arr[min_index]:
                    min_index = j

            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

        return arr
                    




s1 = Solution()

n_1 = [10,4,5,7,8,2,1]

print(s1.selection_sort(n_1))
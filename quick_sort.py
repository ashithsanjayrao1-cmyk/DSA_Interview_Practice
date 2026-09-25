class Solution():
    def quick_sort(self,arr,low,high):
        if low < high:
            pIndex = self.partition(arr,low,high)

            self.quick_sort(arr,low,pIndex-1)
            self.quick_sort(arr,pIndex+1,high)

    def partition(self,arr,low,high):
        pivot = arr[low]
        i = low
        j = high


        while(i<j):
            while(arr[i] <= pivot and i <= high-1):
                i += 1

            while(arr[j] >= pivot and j >= low+1):
                j-=1

            if i<j:
                arr[i],arr[j] = arr[j],arr[i]


        arr[low],arr[j] = arr[j],arr[low]

        return j





s1 = Solution()

my_array = [10, 4, 5, 7, 8, 2, 1]

s1.quick_sort(my_array, 0, len(my_array) - 1)
print(my_array)
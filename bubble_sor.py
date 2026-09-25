class Solution():
    def bubble_sort(self,arr):

        loop_count = 0

        n = len(arr)

        for i in range(n-1):
            did_swap = False
            loop_count +=1 
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    temp =  arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp

                    did_swap = True

            if not did_swap:
                break

        print(f"Total outer loops executed: {loop_count}")

        return arr

s1 = Solution()

n_1 = [10,4,5,7,8,2,1]


print(s1.bubble_sort(n_1))

sorted_arr = [1,2,3,4,5,6,7,8]

print(s1.bubble_sort(sorted_arr))



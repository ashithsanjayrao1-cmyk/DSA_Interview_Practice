class Solution():
    def reverse_pairs(self,arr):
        n = len(arr)

        count = 0

        for i in range(n):

            for j in range(i+1,n):

                if arr[i] > 2* arr[j]:
                    count +=1

        return count


s1 = Solution()

arr = [6,4,1,2,6]

print(s1.reverse_pairs(arr))

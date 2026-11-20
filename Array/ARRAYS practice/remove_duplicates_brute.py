class Solution():
    def RemoveDuplicates(self,arr):
        n = len(arr)
        unique_elements= set()

        for i in range(n):
            unique_elements.add(arr[i])

        index = 0

        for it in sorted(unique_elements):
            arr[index] = it
            index += 1

        return index

s1 = Solution()

print(s1.RemoveDuplicates(arr=[1,1,2,2,3,3]))

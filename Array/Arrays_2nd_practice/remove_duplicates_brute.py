class Solution():
    def removeDuplicates(self,arr):
        n  = len(arr)

        st = set(arr)

        for i in range(n):
            st.add(arr[i])

        sorted_st = sorted(st)

        index = 0

        for it in sorted_st:
            arr[index] = it
            index += 1
        return index
s1 = Solution()
arr = [1,1,2,2,3,3,4,4,4,5,5,6]
print(s1.removeDuplicates(arr))
    


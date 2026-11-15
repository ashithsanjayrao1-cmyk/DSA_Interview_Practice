class Solution():
    def union(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        st = set()
        union = []

        for i in range(n1):
            st.add(arr1[i])
        for i in range(n2):
            st.add(arr2[i])

        for val in st:

            union.append(val)
        return union
s1 = Solution()
print(s1.union(arr1=[1,2,3,4,5,1],arr2=[2,3,3,2,4,5,5,5,5]))


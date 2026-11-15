class Solution():
    def missing(self,arr):
        asn = -1
        n = len(arr)

        for i in range(n):
            flag = 0
            for j in range(n):
                if arr[j]== i:

                    flag = 1
                    break

        if flag == 0:
            return i
        return i
s1 = Solution()
print(s1.missing([1,3,4,5]))


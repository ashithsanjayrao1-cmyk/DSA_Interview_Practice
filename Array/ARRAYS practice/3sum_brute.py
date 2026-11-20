class Solution():
    def threeSum(self,arr):

        n = len(arr)

        unique_triplets = set()

        for i in range(n):
            for j in range(i+1,n):

                for k in range(j+1,n):
                    

                    if arr[i] + arr[j] + arr[k] == 0:

                        tripler = tuple(sorted((arr[i],arr[j],arr[k])))
                        unique_triplets.add(tripler)

        return[list(t) for t in unique_triplets]

s1 = Solution()
arr = [-1, 0, 1, 2, -1, -4]
print(s1.threeSum(arr))
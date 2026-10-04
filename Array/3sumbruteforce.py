class Solution():
    def threesum(self,arr):
        n = len(arr)

        unique_triplets = set()


        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        temp = [arr[i] , arr[j],arr[k]]

                        temp.sort()

                        unique_triplets.add(tuple(temp))


        ans = [list(triplet) for triplet in unique_triplets]
        return ans


s1 = Solution()

arr = [-1, 0, 1, 2, -1, -4]

print(s1.threesum(arr))


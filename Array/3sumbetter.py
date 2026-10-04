class Solution():
    def threesum(self,arr):
        n = len(arr)

        unique_treplets = set()

        for i in range(n):

            seen = set()

            for j in range(i+1,n):
                needed = -(arr[i] + arr[j])


                if needed in seen:
                    temp = [arr[i],arr[j],needed]
                    temp.sort()

                    unique_treplets.add(tuple(temp))

                seen.add(arr[j])


        ans = [list(triplet) for triplet in unique_treplets]

        return ans

s1 = Solution()
arr = [-1, 0, 1, 2, -1, -4]
print(s1.threesum(arr))

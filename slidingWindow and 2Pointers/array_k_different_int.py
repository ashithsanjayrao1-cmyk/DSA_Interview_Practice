class Solution():
    def DifferentIntegers(self,arr:list[int],k:int) -> int:

        n = len(arr)

        count = 0

        for i in range(n):

            uniquemap = {}

            for j in range(i,n):

                uniquemap[arr[j]] = uniquemap.get(arr[j],0)+1
                if len(uniquemap) == k:

                    count += 1

                elif len(uniquemap) > k:
                    break


        return count

s1 = Solution()

arr = [1,2,1,3,4]

k = 3

print(s1.DifferentIntegers(arr,k))
                
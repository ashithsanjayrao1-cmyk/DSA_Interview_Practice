class Solution():
    def fourSum(self,arr,target):

        unique_quads = set()
        n = len(arr)

        for i in range(n):
            for j in range(i+1,n):
                seen = set()
                for k in range(j+1,n):
                    needed = target - (arr[i]+arr[j]+arr[k])

                    if needed in seen:

                        temp = [arr[i],arr[j],arr[k],needed]

                        temp.sort()

                        unique_quads.add(tuple(temp))

                    seen.add(arr[k])

        ans = [list(quad) for quad in unique_quads]

        return ans

s1 = Solution()

arr = [1,0,-1,0,-2,2]
target = 0

print(s1.fourSum(arr,target))





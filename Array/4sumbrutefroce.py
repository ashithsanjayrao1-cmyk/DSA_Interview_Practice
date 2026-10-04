class Solution():

    def foursum(self,arr,target):
        n = len(arr)

        unique_quads = set()

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        if arr[i] + arr[j] + arr[k] + arr[l] == target:
                            temp = [arr[i],arr[j],arr[k],arr[l]]
                            temp.sort()

                            unique_quads.add(tuple(temp))


        ans = [list(quad) for quad in unique_quads]
        return ans


s1 = Solution()
arr = [1, 0, -1, 0, -2, 2]
target = 0
print(s1.foursum(arr, target))

        


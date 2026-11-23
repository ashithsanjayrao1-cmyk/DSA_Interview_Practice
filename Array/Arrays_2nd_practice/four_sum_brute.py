class Solution():
    def fourSum(self,arr,target):
        n = len(arr)
        quaruplets = set()

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):

                        if arr[i]+arr[j]+arr[k]+arr[l] == target:
                            temp = [arr[i],arr[j],arr[k],arr[l]]

                            temp.sort()

                            quaruplets.add(tuple(temp))

        return [list(quad) for quad in quaruplets]
s1 = Solution()
print(s1.fourSum([1,-2,3,5,7,9],7))



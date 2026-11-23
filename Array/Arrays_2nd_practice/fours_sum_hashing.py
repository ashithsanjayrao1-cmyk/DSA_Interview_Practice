class Solution():
    def fourSum(self,arr,target):

        n = len(arr)

        quadraplets = set()

        for i in range(n):
            for j in range(i+1,n):
                seen_element = set()

                for k in range(j+1,n):
                    needed = target - (arr[i]+arr[j]+arr[k])

                    if needed in seen_element:

                        temp = [arr[i],arr[j],arr[k],needed]
                        temp.sort()

                        quadraplets.add(tuple(temp))

                    seen_element.add(arr[k])

        return [list(quad) for quad in quadraplets]
s1 = Solution()
print(s1.fourSum([1,1,3,4,-3],5))
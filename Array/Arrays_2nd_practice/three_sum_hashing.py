class Solution():
    def Threesum(self,arr):
        n = len(arr)
        unique_set = set()

        for i in range(n):

            seen = set()

            for j in range(i+1,n):
                needed = -(arr[i] + arr[j])

                if needed in seen:
                    temp = [arr[i],arr[j],needed]
                    temp.sort()

                    unique_set.add(tuple(temp))

                    
                seen.add(arr[j])
        return [list(t) for t in unique_set ]
    
s1= Solution()
print(s1.Threesum([2,-2,0,3,-3,5]))
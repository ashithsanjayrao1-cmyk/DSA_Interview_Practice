class Solution():
    def rearrange(self,arr):
        n = len(arr)

        pos = []
        neg = []
        ans = []

        for i in range(n):
            if arr[i] < 0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])


        for i in range(n//2):
            # ans.append(pos[i])
            # ans.append(neg[i])

            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        return arr

s1 = Solution()
print(s1.rearrange([2,4,5,-1,-3,-4]))

class Solution():
    def rearrange(self,arr):
        n = len(arr)

        ans = [0] * n 

        pos_index = 0
        neg_index = 1

        for i in range(n):
            if arr[i] > 0:
                ans[pos_index] = arr[i]
                pos_index += 2

            else:
                ans[neg_index] = arr[i]
                neg_index += 2

        return ans




        # pos = []

        # neg = []

        # for i in range(n):
        #     if arr[i] > 0:
        #         pos.append(arr[i])

        #     else:
        #         neg.append(arr[i])

        # for i in range(n//2):
        #     arr[2*i] = pos[i]

        #     arr[2*i+1] = neg[i]

        # return arr

s1 = Solution()

arr = [3,1,-2,-5,2,-4]

print(s1.rearrange(arr))
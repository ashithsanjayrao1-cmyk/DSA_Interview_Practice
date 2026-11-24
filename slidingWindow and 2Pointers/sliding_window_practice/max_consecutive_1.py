class Solution():
    def max_consecutive_1(self,arr,k):

        n = len(arr)
        max_len = 0

        for i in range(n):
            zeroes = 0
            for j in range(i,n):
                if arr[j] == 0:
                    zeroes +=1
                if zeroes <=k:
                    curr_len = j-i+1
                    max_len = max(curr_len,max_len) 
                else:
                    break
        return max_len
s1 = Solution()
print(s1.max_consecutive_1([1,1,1,0,0,0,1,1,1,1,0],2))
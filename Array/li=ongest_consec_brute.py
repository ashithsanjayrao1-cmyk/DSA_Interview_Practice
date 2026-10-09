class Solution():
    def ls(self,arr,num):
        for i in range(len(arr)):
            if arr[i] == num:
                return True

        return False


    def longestConsecutive(self,arr):
        n = len(arr)

        if n == 0:
            return 0

        longest = 1

        for i in range(n):
            x = arr[i]

            cnt = 1

            while self.ls(arr,x+1) == True:
                x = x+1
                cnt += 1

            if longest < cnt:
                longest = cnt

            # longest = max(longest, cnt)


        return longest


s1 = Solution()
arr = [100, 4, 200, 1, 3, 2]
print(s1.longestConsecutive(arr))


            


        
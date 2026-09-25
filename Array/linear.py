class Solution():

    def Linear(self,arr,num,n):
        for i in range(n):
            if arr[i] == num:
                return i

        return -1

s1 = Solution()

arr = [2,3,4,5,6,7]

num = 8

n = 6

output = s1.Linear(arr,num,n)

print(output)
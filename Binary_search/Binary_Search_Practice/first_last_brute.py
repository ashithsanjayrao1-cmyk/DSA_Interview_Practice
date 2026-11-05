class Solution():
    def firstLast(self,arr,x):
        n = len(arr)
        first = -1
        last = -1

        for i in range(n):
            if arr[i] == x:
                if first == -1:
                    first = i

                else:
                    last = i

        return first,last

s1 = Solution()
arr = [3,4,4,7,8,10]
x = 3

print(s1.firstLast(arr,x))
 
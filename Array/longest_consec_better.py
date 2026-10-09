class Solution():
    def longestConsecutive(slef,arr):
        n = len(arr)

        if n == 0:
            return 0


        arr.sort()

        last_smaller = float('-inf')

        count = 0

        longest = 1

        for i in range(n):
            if arr[i] -1 == last_smaller:
                count += 1
                last_smaller = arr[i]

            elif arr[i] != last_smaller:
                count = 1

                last_smaller = arr[i]

            longest = max(longest,count)

        return longest

s1 = Solution()
arr = [100, 4, 200, 1, 3, 2]
print(s1.longestConsecutive(arr))
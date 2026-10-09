class SOlution():

    def longestConsecutiveOptimal(self,arr):

        n = len(arr)

        if not arr:
            return 0

        num_set = set(arr)

        longest = 1

        for arr in num_set:

            if arr -1 not in num_set:

                current_num = arr
                count = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1

                longest= max(longest,count)

        return longest
s1 = SOlution()
nums = [100, 4, 200, 1, 3, 2]
print(s1.longestConsecutiveOptimal(nums))
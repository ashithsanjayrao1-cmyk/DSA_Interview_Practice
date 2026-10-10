class Solution():
    def countSubarrayOptimal(self,arr,k):
        n = len(arr)

        xor_map = {0:1}

        count = 0

        current_xor = 0

        for i in range(n):
            current_xor ^= arr[i]

            x = current_xor ^ k

            if x in xor_map:
                count += xor_map[x]

            if current_xor in xor_map:
                xor_map[current_xor] += 1

            else:
                xor_map[current_xor] = 1

        return count


s1 = Solution()
arr = [4, 2, 2, 6, 4]
k = 6

print(s1.countSubarrayOptimal(arr,k))

    
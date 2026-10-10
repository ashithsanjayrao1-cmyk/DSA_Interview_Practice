class SOlution():
    def longestSubarrayk2pointer(self,arr,k):

        n = len(arr)
        left = 0
        right = 0 
        max_len = 0


        current_sum = arr[0]

        while right < n:
            while left <= right and current_sum >k:
                current_sum -= arr[left]

                left+=1

            if current_sum == k:
                max_len = max(max_len,right-left + 1)

            right += 1
            if right < n:
                current_sum += arr[right]

        return max_len

s1 = SOlution()
arr = [1, 2, 3, 1, 1, 1, 1]
k = 3

print(s1.longestSubarrayk2pointer(arr,k))


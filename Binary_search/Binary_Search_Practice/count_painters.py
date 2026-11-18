class Solution():
    def func(self,arr,time_limit):
        painters = 1

        current_board = 0

        n = len(arr)
        for i in range(n):

            if current_board + arr[i] > time_limit:
                painters+=1
                current_board = arr[i]

            else:
                current_board += arr[i]

        return painters


    def paint(self, A: int, B: int, C: list[int]) -> int:

        low = max(C)
        high = sum(C)

        while low <= high:
            mid = (low+high)//2

            count = self.func(C,mid)

            if count <= A:
                high = mid-1

            else:
                low = mid+1

        return (low*B) % 1000003          

s1 = Solution()
print(s1.paint(2,5,[1,10]))  
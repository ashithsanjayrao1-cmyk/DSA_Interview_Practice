class Solution():

    def countpainters(self,boards,time_limit):
        painters = 1
        current_board = 0

        for board in boards:
            if current_board + board > time_limit:
                painters += 1
                current_board = board
            else:
                current_board += board

        return painters

    def findLargestMinDistance(self,boards,k):

        low = max(boards)

        high = sum(boards)

        ans = -1

        while low <= high:
            mid = (low+high)//2

            if self.countpainters(boards,mid) <= k:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans

s1 = Solution()
boards = [10, 20, 30, 40]
k = 2

print(s1.findLargestMinDistance(boards,k))
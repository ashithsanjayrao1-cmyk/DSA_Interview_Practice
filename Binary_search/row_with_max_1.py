class SOlution():
    def maxRow(self,arr,n,m):
        index = -1
        max_count = -1
        

        for i in range(n):
            count_row = 0

            for j in range(m):
                count_row += arr[i][j]

            if count_row > max_count:
                max_count = count_row
                index = i

        return index
    
s1 = SOlution()
arr = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

print(s1.maxRow(arr,4,4))


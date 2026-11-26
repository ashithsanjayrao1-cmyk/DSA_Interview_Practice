class Job:
    def __init__(self,id,deadline,profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution():
    def jobSequencingProblem(self,arr):
        n = len(arr)


        arr.sort(key = lambda x: x.profit,reverse = True)


        total_profit = 0
        count_profit = 0
        max_deadline = -1

        for i in range(0,n):
            max_deadline = max(max_deadline,arr[i].deadline)

        hash_arr = [-1] * (max_deadline+1)


        for i in range(n):

            for j in range(arr[i].deadline,0,-1):

                if hash_arr[j] == -1:
                    count_profit += 1
                    hash_arr[j] = arr[i].id

                    total_profit += arr[i].profit
                    break
        return (count_profit,total_profit)


if __name__ == "__main__":
    # Format: Job(id, deadline, profit)
    job1 = Job(1, 4, 20)
    job2 = Job(2, 5, 60)
    job3 = Job(3, 6, 70)
    job4 = Job(4, 6, 65)
    job5 = Job(5, 4, 25)
    job6 = Job(6, 2, 80)
    job7 = Job(7, 2, 10)
    job8 = Job(8, 2, 22)

    arr = [job1, job2, job3, job4, job5,job6,job7,job8]
    
    s = Solution()
    jobs_done, max_profit = s.jobSequencingProblem(arr)
    
    print(f"Total jobs completed: {jobs_done}")
    print(f"Maximum profit earned: {max_profit}")
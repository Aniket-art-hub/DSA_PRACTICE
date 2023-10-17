class JobScheduling:
    class Job:
        def __init__(self, jobid, deadline, profit):
            self.id = jobid
            self.deadline = deadline
            self.profit = profit

    class ProfitComparator:
        def __call__(self, j):
            return j.profit

    def jobScheduling(self, arr, n):
        jobList = arr.copy()
        jobList.sort(key=self.ProfitComparator(), reverse=True)

        slotFilled = [False] * (n + 1)
        profit = 0
        slotUsed = 0

        for job in jobList:
            deadline = job.deadline
            while deadline > 0 and slotFilled[deadline]:
                deadline -= 1
            if deadline > 0:
                profit += job.profit
                slotFilled[deadline] = True
                slotUsed += 1

        return [slotUsed, profit]

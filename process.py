class process:
    def __init__(self, pid, arrival, burst,priority = 0):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.start = 0
        self.completion = 0
        self.waiting = 0
        self.turnaround = 0
        self.priority = priority
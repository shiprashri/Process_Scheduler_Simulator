from collections import deque
def round_robin(processes , quantum):
    procs = sorted(processes, key=lambda p: p.arrival)
    remaining_burst = {p.pid: p.burst for p in procs}
    clock = 0
    queue = deque()
    completed = []
    i = 0
    while i < len(procs) and procs[i].arrival <= clock:
        queue.append(procs[i])
        i += 1
    while queue :
        current = queue.popleft()
        if remaining_burst[current.pid] == current.burst:
            current.start = clock
        run_time = min(quantum , remaining_burst[current.pid])
        clock += run_time
        remaining_burst[current.pid] -= run_time
        while i < len(procs) and procs[i].arrival <= clock:
            queue.append(procs[i])
            i += 1
        if remaining_burst[current.pid] > 0:
            queue.append(current)
        else :
            current.completion = clock
            current.turnaround = current.completion - current.arrival
            current.waiting = current.turnaround - current.burst
            completed.append(current)
    return completed
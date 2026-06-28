def fcfs(processes):
    procs = sorted(processes, key=lambda p: p.arrival)
    clock = 0
    for p in procs:
        if clock < p.arrival:
            clock = p.arrival
        p.start = clock
        clock = clock + p.burst
        p.completion = clock
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst
    return procs
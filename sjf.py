def sjf(processes):
    procs = processes.copy()
    completed = []
    clock = 0
    while procs :
        available = [p for p in procs if p.arrival <= clock]
        if not available:
            clock = min(p.arrival for p in procs)
            continue
        current = min(available , key = lambda p: p.burst)
        current.start = clock
        clock += current.burst
        current.completion = clock
        current.turnaround = current.completion - current.arrival
        current.waiting = current.turnaround - current.burst
        completed.append(current)
        procs.remove(current)
    return completed
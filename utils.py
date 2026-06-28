def print_gantt(procs):
    print("\nGantt Chart:")
    top = ""
    bottom = ""
    for p in procs:
        block = f"P{p.pid}".center(8)
        top += "|" + block
        bottom += f"{p.start}".ljust(9)
    top += "|"
    bottom += f"{procs[-1].completion}"
    print(top)
    print(bottom)

def print_table(procs):
    print(f"\n{'PID':<5}{'Arrival':<10}{'Burst':<8}{'Completion':<12}{'Waiting':<10}{'Turnaround':<12}")
    total_wt = 0
    total_tat = 0
    for p in procs:
        print(f"{p.pid:<5}{p.arrival:<10}{p.burst:<8}{p.completion:<12}{p.waiting:<10}{p.turnaround:<12}")
        total_wt += p.waiting
        total_tat += p.turnaround
    n = len(procs)
    print(f"\nAverage Waiting Time: {total_wt/n:.2f}")
    print(f"Average Turnaround Time: {total_tat/n:.2f}")
from process import process
from fcfs import fcfs
from sjf import sjf
from priority import priority_scheduling
from round_robin import round_robin
from utils import print_gantt, print_table


def get_processes_from_user():
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(1, n + 1):
        print(f"\nProcess {i}:")
        arrival = int(input("  Arrival time: "))
        burst = int(input("  Burst time: "))
        priority = int(input("  Priority (lower = more important, default 0): ") or 0)
        processes.append(process(i, arrival, burst, priority))
    return processes


def run_algorithm(choice, processes, quantum=None):
    if choice == "1":
        print("\n===== FCFS =====")
        result = fcfs(processes)
    elif choice == "2":
        print("\n===== SJF (Non-Preemptive) =====")
        result = sjf(processes)
    elif choice == "3":
        print("\n===== Priority Scheduling =====")
        result = priority_scheduling(processes)
    elif choice == "4":
        if quantum is None:
            quantum = int(input("Enter time quantum: "))
        print(f"\n===== Round Robin (quantum={quantum}) =====")
        result = round_robin(processes, quantum)
    else:
        print("Invalid choice.")
        return

    print_gantt(result)
    print_table(result)


if __name__ == "__main__":
    print("Process Scheduler Simulator")
    print("1. FCFS")
    print("2. SJF (Non-Preemptive)")
    print("3. Priority Scheduling")
    print("4. Round Robin")

    choice = input("\nChoose an algorithm (1-4): ").strip()

    processes = get_processes_from_user()

    run_algorithm(choice, processes)
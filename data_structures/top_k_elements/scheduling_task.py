"""
You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU
interval to execute but once a task has finished, it has a cooling period during which it can’t be run again.
If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

example1:
    Input: [a, a, a, b, c, c], K=2
    Output: 7
    Explanation: a -> c -> b -> a -> c -> idle -> a

example2:
    Input: [a, b, a], K=3
    Output: 5
    Explanation: a -> b -> idle -> idle -> a
"""

import heapq


def schedule_tasks(tasks, k):
    intervalCount = 0
    task_freq_map = {}
    for task in tasks:
        if task not in task_freq_map:
            task_freq_map[task] = 0
        task_freq_map[task] += 1

    max_heap = []
    for key, val in task_freq_map.items():
        heapq.heappush(max_heap, (-val, key))

    while max_heap:
        waiting_list = []
        n = k + 1
        while n > 0 and max_heap:
            freq, char = heapq.heappop(max_heap)
            intervalCount += 1
            if -freq > 1:
                waiting_list.append((char, freq + 1))
            n -= 1

        for key, val in waiting_list:
            heapq.heappush(max_heap, (val, key))

        if max_heap:
            intervalCount += n

    return intervalCount


def main():
    print(
        "Minimum intervals needed to execute all tasks: "
        + str(schedule_tasks(["a", "a", "a", "b", "c", "c"], 2))
    )
    print(
        "Minimum intervals needed to execute all tasks: "
        + str(schedule_tasks(["a", "b", "a"], 3))
    )


main()

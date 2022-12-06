"""
You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei]
means that the ith task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:
1. If the CPU is idle and there are no available tasks to process, the CPU remains idle.
2. If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time.
If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
3. Once a task is started, the CPU will process the entire task without stopping.
4. The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.
"""

from typing import List

import heapq


def getOrder(tasks: List[List[int]]) -> List[int]:
    order_indexes = []
    enqueued_tasks = []
    available_tasks = []
    for i in range(len(tasks)):
        heapq.heappush(enqueued_tasks, (tasks[i][0], tasks[i][1], i))

    first_task = heapq.heappop(enqueued_tasks)
    total_time = first_task[1] + first_task[0]
    order_indexes.append(first_task[2])
    while enqueued_tasks:
        while enqueued_tasks and enqueued_tasks[0][0] <= total_time:
            pop = heapq.heappop(enqueued_tasks)
            heapq.heappush(available_tasks, (pop[1], pop[2], pop[0]))
        if not available_tasks:
            total_time = enqueued_tasks[0][0]
            continue
        else:
            pop = heapq.heappop(available_tasks)
            total_time += pop[0]
            order_indexes.append(pop[1])

    while available_tasks:
        pop = heapq.heappop(available_tasks)
        order_indexes.append(pop[1])

    return order_indexes


print(getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
print(getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))

print(getOrder([[1, 2], [8, 5], [3, 2], [4, 1]]))

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

import math


def getOrder(tasks: List[List[int]]) -> List[int]:
    least_enqueue_time = math.inf
    order_indexes = []
    min_heap = []
    for task in tasks:
        least_enqueue_time = min(least_enqueue_time, task[0])

    for idx in range(len(tasks)):
        if tasks[idx][0] == least_enqueue_time:
            heapq.heappush(min_heap, (tasks[idx][1], idx, tasks[idx][0]))

    first_processed = heapq.heappop(min_heap)
    processing_time = first_processed[0]
    processed_idx = first_processed[1]
    enqueu_time = first_processed[2]
    total_time = enqueu_time + processing_time
    order_indexes.append(processed_idx)
    while min_heap:
        heapq.heappop(min_heap)

    for idx in range(len(tasks)):
        if idx != processed_idx:
            heapq.heappush(min_heap, (tasks[idx][1], idx, tasks[idx][0]))

    temp = []
    while min_heap:
        top = min_heap[0]
        enqueu_time = top[2]
        if enqueu_time <= total_time:
            pop = heapq.heappop(min_heap)
            processed_idx = pop[1]
            order_indexes.append(processed_idx)
            total_time = pop[0] + pop[2]
            for item in temp:
                heapq.heappush(min_heap, item)
            temp = []
        else:
            while min_heap:
                top = min_heap[0]
                enqueu_time = top[2]
                if enqueu_time > total_time:
                    pop = heapq.heappop(min_heap)
                    temp.append(pop)
                else:
                    break

    return order_indexes


print(getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]))
print(getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))

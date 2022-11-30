"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time,
the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array),
that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation:
        A -> B -> idle -> A -> B -> idle -> A -> B
        There is at least 2 units of time between any two same tasks.
"""

import heapq


def least_interval(tasks, n) -> int:
    if n == 0:
        return len(tasks)
    max_heap = []
    tasks_occurrences = {}
    for task in tasks:
        if task not in tasks_occurrences:
            tasks_occurrences[task] = 0

        tasks_occurrences[task] += 1

    for key, val in tasks_occurrences.items():
        heapq.heappush(max_heap, (-val, key))

    intervals = 0
    while max_heap:
        items = n + 1
        waiting_list = []
        while items > 0 and max_heap:
            temp = heapq.heappop(max_heap)
            freq = temp[0]
            char = temp[1]
            intervals += 1
            if -freq > 1:
                waiting_list.append((freq + 1, char))
            items -= 1
        for val in waiting_list:
            heapq.heappush(max_heap, val)

        if max_heap:
            intervals += items

    return intervals


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(least_interval(tasks, n))

tasks = ["A", "A", "A", "B", "B", "B"]
n = 0
print(least_interval(tasks, n))

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(least_interval(tasks, n))

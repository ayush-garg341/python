"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

example1:
    Jobs: [[1,4,3], [2,5,4], [7,9,6]]
    Output: 7

example2:
    Jobs: [[6,7,10], [2,4,11], [8,12,15]]
    Output: 15

"""

from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on job.end
        return self.end < other.end


def find_max_cpu_load(jobs):
    max_load = 0
    current_load = 0

    jobs.sort(key=lambda x: x.start)

    min_heap = []

    for job in jobs:
        while len(min_heap) and job.start >= min_heap[0].end:
            top = heappop(min_heap)
            current_load -= top.cpu_load
            max_load = max(max_load, current_load)
        current_load += job.cpu_load
        max_load = max(max_load, current_load)
        heappush(min_heap, job)
    return max_load


print(
    "Maximum CPU load at any time: "
    + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)]))
)
print(
    "Maximum CPU load at any time: "
    + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)]))
)
print(
    "Maximum CPU load at any time: "
    + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)]))
)

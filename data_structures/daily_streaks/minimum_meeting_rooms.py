"""
Given a list of intervals representing the start and end time of ‘N’ meetings,
find the minimum number of rooms required to hold all the meetings.

ex1:
    Meetings: [[1,4], [2,5], [7,9]]
    Output: 2
    Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
    occur in any of the two rooms later.

ex2:
    Meetings: [[4,5], [2,3], [2,4], [3,5]]
    Output: 2
    Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

ex3:
    Meetings: [[1,4], [2,3], [3,6]]
    Output:2
    Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to
    hold all the meetings.
"""

from heapq import *

def min_meetings_room(meetings):
    ending_times_heap = []
    meetings.sort()
    for i in range(len(meetings)):
        if len(ending_times_heap) == 0:
            heappush(ending_times_heap, meetings[i][1])
        else:
            next_start = meetings[i][0]
            top = ending_times_heap[0]
            if next_start < top:
                heappush(ending_times_heap, meetings[i][1])
            else:
                heappop(ending_times_heap)
                heappush(ending_times_heap, meetings[i][1])

    return len(ending_times_heap)


print(min_meetings_room([[1,4], [2,5], [7,9]]))
print(min_meetings_room([[6,7], [2,4], [8,12]]))
print(min_meetings_room([[1,4], [2,3], [3,6]]))
print(min_meetings_room([[4,5], [2,3], [2,4], [3,5]]))

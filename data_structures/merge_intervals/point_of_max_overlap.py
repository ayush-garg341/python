"""
Given a list of intervals, find the point where the maximum number of intervals overlap.

This problem follows min_meeting_rooms pattern.
"""
import heapq


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def point_of_max_overlap(meetings):
    meetings.sort(key=lambda x: x.start)
    min_heap = []
    max_overlap = 0
    point_of_time = meetings[0].start

    for meet in meetings:

        while len(min_heap) > 0 and meet.start > min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, meet.end)

        if len(min_heap) > max_overlap:
            max_overlap = len(min_heap)
            point_of_time = meet.start

    return (point_of_time, max_overlap)


point, max_overlap = point_of_max_overlap([Meeting(1, 4), Meeting(2, 5), Meeting(9, 12), Meeting(5, 9), Meeting(5, 12)])
print("There are maximum of {} people at time {}".format(max_overlap, point))
point, max_overlap = point_of_max_overlap(
    [
        Meeting(13, 107),
        Meeting(28, 95),
        Meeting(29, 111),
        Meeting(14, 105),
        Meeting(40, 70),
        Meeting(17, 127),
        Meeting(3, 74),
    ]
)
print("There are maximum of {} people at time {}".format(max_overlap, point))

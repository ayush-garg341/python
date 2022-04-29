"""
Given a list of intervals representing the start and end time of ‘N’ meetings,
find the minimum number of rooms required to hold all the meetings.

example1:
    Meetings: [[1,4], [2,5], [7,9]]
    Output: 2
    Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can
    occur in any of the two rooms later.

example2:
    Meetings: [[6,7], [2,4], [8,12]]
    Output: 1
    Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

example3:
    Meetings: [[4,5], [2,3], [2,4], [3,5]]
    Output: 2
    Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

Similar problem:-
Given a list of intervals representing the arrival and departure times of trains to a train station, our goal is to
find the minimum number of platforms required for the train station so that no train has to wait.
"""

import heapq


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms_wrong(meetings):
    min_rooms = 1
    end_time = {}
    meetings.sort(key=lambda x: x.start)

    end_time[meetings[0].end] = 1
    for i in range(1, len(meetings)):
        if meetings[i].start < meetings[i - 1].end:
            if meetings[i].start not in end_time:
                min_rooms += 1

        end_time[meetings[i].end] = 1

    return min_rooms


print("Minimum meeting rooms required: " + str(min_meeting_rooms_wrong([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
print("Minimum meeting rooms required: " + str(min_meeting_rooms_wrong([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
print("Minimum meeting rooms required: " + str(min_meeting_rooms_wrong([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
print(
    "Minimum meeting rooms required: "
    + str(min_meeting_rooms_wrong([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))
)


def min_meeting_rooms(meetings):
    min_rooms = 0
    meetings.sort(key=lambda x: x.start)

    min_heap = []
    for meet in meetings:
        while len(min_heap) > 0 and meet.start >= min_heap[0]:
            # when we are removing the element from heap, it means new meeting is taking place in already booked room.
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, meet.end)
        min_rooms = max(min_rooms, len(min_heap))
    return min_rooms


print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
print("Minimum meeting rooms required: " + str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
print(
    "Minimum meeting rooms required: "
    + str(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))
)

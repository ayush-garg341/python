"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

example1:
    Appointments: [[1,4], [2,5], [7,9]]
    Output: false
    Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

example2:
    Appointments: [[6,7], [2,4], [8,12]]
    Output: true
    Explanation: None of the appointments overlap, therefore a person can attend all of them.

example3:
    Appointments: [[4,5], [2,3], [3,6]]
    Output: false
    Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

"""


def can_attend_all_appointments(intervals):
    if len(intervals) < 2:
        return True
    intervals.sort()
    first_elt = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] < first_elt[1]:
            return False
        else:
            first_elt = intervals[i]

    return True


print(
    "Can attend all appointments: "
    + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))
)
print(
    "Can attend all appointments: "
    + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]]))
)
print(
    "Can attend all appointments: "
    + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))
)

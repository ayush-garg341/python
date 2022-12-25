"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

ex1: input - [[1,4], [2,5], [7,9]]
    output - false

ex2: input - [[6,7], [2,4], [8,12]]
    output - true

ex3: input - [[4,5], [2,3], [3,6]]
    output - false
"""


def can_attend_all_appointments(intervals):
    """
    TC -> O(NlogN)
    """
    intervals.sort(key=lambda x: x[0])
    temp = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= temp[0] and intervals[i][0] < temp[1]:
            return False
        else:
            temp = intervals[i]
    return True


"""
Given a list of appointments, find all the conflicting appointments.
ex1: input [[4,5], [2,3], [3,6], [5,7], [7,8]]
    [4,5] and [3,6] conflict, [3,6] and [5,7] conflict.
"""


def find_all_conflicting_appointments(intervals):
    intervals.sort(key=lambda x: x[0])


def main():
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


main()

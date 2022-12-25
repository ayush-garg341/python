"""
For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
Our goal is to find out if there is a free interval that is common to all employees.
You can assume that each list of employee working hours is sorted on the start time.

example1:
    Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
    Output: [3,5]
    Explanation: Both the employees are free between [3,5].
"""

from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def find_employee_free_time(schedule):
    result = []
    # TODO: Write your code here
    flatten_intervals = []
    for empl in schedule:
        for interval in empl:
            flatten_intervals.append(interval)

    flatten_intervals.sort(key=lambda x: x.start)
    start_interval = flatten_intervals[0]
    max_end_time_so_far = start_interval.end
    for i in range(1, len(flatten_intervals)):
        if flatten_intervals[i].start <= start_interval.end:
            max_end_time_so_far = max(max_end_time_so_far, flatten_intervals[i].end)
            start_interval = flatten_intervals[i]
        else:
            if flatten_intervals[i].start > max_end_time_so_far:
                interval = Interval(max_end_time_so_far, flatten_intervals[i].start)
                result.append(interval)
            start_interval = flatten_intervals[i]
            max_end_time_so_far = max(max_end_time_so_far, flatten_intervals[i].end)

    return result


def main():
    input = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end="")
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()

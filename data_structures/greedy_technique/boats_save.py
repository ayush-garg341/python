"""
Minimum number of life saving boats to evacuate people.
Two people at a time in boat and each people's weight is less than boat limit.
"""


def rescue_boats(people, limit):
    """
    people:- weight array of people
    """
    people.sort()

    l = 0
    r = len(people) - 1
    boats = 0
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        boats += 1

    return boats

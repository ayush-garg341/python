"""
Given an array of buildings and direction that all of the buildings face, return an array of indices of buildings
that can see the sunset.
A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction
that it faces.

east -> right
west -> left

example1:
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "EAST"
    output = [1, 3, 6, 7]

example2:
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    direction = "WEST"
    output = [0, 1]
"""


def sunsetViews(buildings, direction):
    # Write your code here.
    result = []
    n = len(buildings)
    if n == 0:
        return result
    if direction == "EAST":
        for i in range(n - 2, -1, -1):
            buildings[i] = max(buildings[i], buildings[i + 1])

        for i in range(0, n - 1):
            if buildings[i] != buildings[i + 1]:
                result.append(i)
            else:
                continue
        result.append(n - 1)

    if direction == "WEST":
        for i in range(1, n):
            buildings[i] = max(buildings[i], buildings[i - 1])

        result.append(0)
        for i in range(1, n):
            if buildings[i] != buildings[i - 1]:
                result.append(i)
            else:
                continue

    return result


print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST"))


def sunsetViewsCleaner(buildings, direction):
    # Write your code here.
    n = len(buildings)
    result = []
    if n == 0:
        return result
    if direction == "EAST":
        buildings.reverse()

    for i in range(1, n):
        buildings[i] = max(buildings[i], buildings[i - 1])

    result.append(0)
    for i in range(1, n):
        if buildings[i] != buildings[i - 1]:
            result.append(i)

    if direction == "EAST":
        result.reverse()
        return [n - 1 - num for num in result]
    else:
        return result


print(sunsetViewsCleaner([3, 5, 4, 4, 3, 1, 3, 2], "WEST"))

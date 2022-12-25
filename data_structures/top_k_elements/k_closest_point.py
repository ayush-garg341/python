"""
Given an array of points in a 2D plane, find ‘K’ closest points to the origin.

example1:
    Input: points = [[1,2],[1,3]], K = 1
    Output: [[1,2]]
    Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
    The Euclidean distance between (1, 3) and the origin is sqrt(10).
    Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

example2:
    Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
    Output: [[1, 3], [2, -1]]
"""

import heapq


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end="")


def find_closest_points(points, k):
    result = []
    max_heap = []
    n = len(points)
    for i in range(k):
        heapq.heappush(max_heap, [-(points[i].x ** 2 + points[i].y ** 2), points[i]])

    for i in range(k, n):
        distance = -(points[i].x ** 2 + points[i].y ** 2)
        if distance > max_heap[0][0]:
            heapq.heappop(max_heap)
            heapq.heappush(
                max_heap, [-(points[i].x ** 2 + points[i].y ** 2), points[i]]
            )

    while len(max_heap):
        max_elt = heapq.heappop(max_heap)
        result.append(max_elt[1])

    return result


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ")
    for point in result:
        point.print_point()

    result = find_closest_points([Point(1, 3), Point(1, 2)], 1)
    print("Here are the k points closest the origin: ", end="")
    for point in result:
        point.print_point()


main()

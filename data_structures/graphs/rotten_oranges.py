"""
Every minute, any fresh orange that is 4-directionally
adjacent to a rotten orange becomes rotten.
"""

from queue import Queue


def rotten_oranges(grid):
    q = Queue()
    mins = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.put((r, c, 0))

    while not q.empty():
        rr, rc, level = q.get()
        found_fresh = False

        if rr + 1 < rows and grid[rr + 1][rc] == 1:
            found_fresh = True
            q.put((rr + 1, rc, level + 1))
            grid[rr + 1][rc] = 2
        if rr - 1 >= 0 and grid[rr - 1][rc] == 1:
            found_fresh = True
            q.put((rr - 1, rc, level + 1))
            grid[rr - 1][rc] = 2
        if rc + 1 < cols and grid[rr][rc + 1] == 1:
            found_fresh = True
            q.put((rr, rc + 1, level + 1))
            grid[rr][rc + 1] = 2
        if rc - 1 >= 0 and grid[rr][rc - 1] == 1:
            found_fresh = True
            q.put((rr, rc - 1, level + 1))
            grid[rr][rc - 1] = 2

        if found_fresh:
            mins = level + 1

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return -1

    return mins


print(rotten_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(rotten_oranges([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(rotten_oranges([[0, 2]]))
